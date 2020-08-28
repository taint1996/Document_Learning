module Response
  def json_response message, is_success, data, status
    render json: {
      message: message,
      is_success: is_success,
      data: data
    }, status: status
  end

  def json_response_success message, data
    render json: {
      message: message,
      is_success: true,
      data: data,
      status: :ok
    }
  end

  def json_response_error message, status
    render json: {
      message: message,
      is_success: false,
      data: {}
    }, status: status
  end
end