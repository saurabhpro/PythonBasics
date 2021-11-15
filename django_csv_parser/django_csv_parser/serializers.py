from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    """ Serializer for a review to be stored in cvent reviews db"""

    class Meta:
        model = Review
        fields = ('review_id', 'review_text', 'submitted_date', 'venue_id', 'status', 'overall_rating',
                  'ws_user_id', 'ws_user_first_name', 'ws_user_email_id')

    review_id = serializers.UUIDField()
    review_text = serializers.CharField(min_length=10, max_length=3000)
    submitted_date = serializers.DateTimeField(input_formats=(['%d/%m/%y %H:%M', 'iso-8601']))
    venue_id = serializers.IntegerField(min_value=0)
    status = serializers.ChoiceField(choices=Review.REVIEW_APPROVAL_STATUS)
    overall_rating = serializers.IntegerField(min_value=1, max_value=5)
    ws_user_email_id = serializers.EmailField()
    # custom fields
    ws_user_id = serializers.SerializerMethodField()
    ws_user_first_name = serializers.SerializerMethodField()

    @staticmethod
    def validate_ws_user_email_id(value):
        """Validate whether the email id belongs to a valid user in ws"""
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(f'A user with this email {value} does not exist!')

        return value

    @staticmethod
    def get_ws_user_id(data):
        """load the unique id of user from the email id provided"""
        user = User.objects.get(email=data['ws_user_email_id'])
        return user.pk

    @staticmethod
    def get_ws_user_first_name(data):
        """load the name of user from the email id provided"""
        user = User.objects.get(email=data['ws_user_email_id'])
        return user.first_name


class ReviewListSerializer(serializers.ListSerializer):
    """Serializer for creating/updating bulk Reviews"""
    child = ReviewSerializer()

    def to_internal_value(self, data):
        """Override to produce a customized response for bulk apis validation errors"""
        if not self.allow_empty and len(data) == 0:
            message = self.error_messages['empty']
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='empty')

        ret = []
        errors = []
        for item in data:
            try:
                validated = self.child.run_validation(item)
            except ValidationError as exc:
                errors.append(self.__create_validation_error(item, exc.detail))
            else:
                ret.append(validated)

        if any(errors):
            raise ValidationError(errors)

        return ret

    @staticmethod
    def __create_validation_error(item, detail):
        """
        @param item: the item where to fetch the id from
        @param detail: list of errors with reason message string
        @return:  Return error response
        """
        return dict({"status": status.HTTP_400_BAD_REQUEST,
                     "data": detail,
                     "message": f'Validation Errors for Review [{item["review_id"]}]. Please Check Details!'})
