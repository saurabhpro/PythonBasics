import csv
import json
import logging
import re
from typing import List

from django.core.serializers.json import DjangoJSONEncoder
from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from django_csv_parser.django_csv_parser.models import Review
from django_csv_parser.django_csv_parser.serializers import ReviewListSerializer

logger = logging.getLogger(f'twsapps.{__name__}')


class Reviews(ListCreateAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        """POST API to import reviews from a csv file and save it to cvent-reviews system
        NOTE: currently we only validate and prepare the data - actual hookup with cvent will happen in a followup story
        """

        csv_file = request.FILES['file']
        try:
            if csv_file.content_type != 'text/csv':
                raise ValidationError(f'Validation failed, Please ensure you are uploading a CSV file')

            # transform data from csv rows
            reader = list(csv.reader(self.__decode_utf8(csv_file)))
            self.__validate_csv_header(reader.pop(0))
        except ValidationError as exc:
            return Response(status=400, data=exc.detail)

        # serializer to validate and sanitize the data input
        data = self.__transform_data(reader)
        serializer = self.get_serializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            review_list = serializer.data
        except ValidationError as exc:
            return JsonResponse(status=207, data=exc.detail, safe=False)

        """TODO insert actual api call to cvent-reviews"""

        logger.debug(
            'Cvent Reviews API CALL: url {}; request: {}; response: {}'.format(
                "TODO replace this with cvent-reviews url",
                json.dumps(review_list, cls=DjangoJSONEncoder),
                "TODO replace this with cvent-reviews api response"
            )
        )
        return JsonResponse(status=207, data=review_list, safe=False)

    @staticmethod
    def __decode_utf8(input_iterator):
        for line in input_iterator:
            yield line.decode('utf-8')

    @staticmethod
    def __transform_data(reader: List) -> List[Review]:
        reviews = []
        for row in reader[1:]:
            if len(row) > 0 and row[6]:
                review = Review(submitted_date=row[0], venue_id=row[1], ws_user_email_id=row[2], overall_rating=row[3],
                                review_text=row[4], status=row[5], review_id=row[6])
                reviews.append(model_to_dict(review))

        return reviews

    @staticmethod
    def __validate_csv_header(row):
        headers = ['Submitted Timestamp', 'Venue Id', 'Email Address', 'Overall Rating', 'Review Text', 'Status',
                   'Review Id']

        index = 0
        regex = re.compile('[^a-zA-Z ]')
        for header in headers:
            if regex.sub('', row[index]) != header:
                raise ValidationError(
                    f'Validation failed, Please ensure correct cell ordering. '
                    f'Found: [{row[index]}] while Expected: [{header}]. Correct Cell order = {headers}')
            index = index + 1
