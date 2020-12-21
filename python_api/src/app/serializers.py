from rest_framework import serializers


class IMDBSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    year = serializers.DateField(required=False, input_formats=["%Y"])
    plot = serializers.CharField(required=False, max_length=5, min_length=4)

    def validate_plot(self, value):
        msg = "You have to provide one of the following arguments: short or full"
        if not any(value == param for param in ("short", "full")):
            raise serializers.ValidationError(msg)
        return value


class LibrarySerializer(serializers.Serializer):
    book_id = serializers.CharField(
        required=True,
        max_length=13,
        min_length=10,
    )
