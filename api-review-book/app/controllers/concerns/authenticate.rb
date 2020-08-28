module Authenticate
  def current_user
    auth_token = request.headers["auth_token"]
    return unless auth_token
    @current_user = User.find_by authentication_token: auth_token
  end

  def authentication_with_token
    return if current_user
    json_response_error "Unauthenticated", :unauthorized
  end
end