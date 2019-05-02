# frozen_string_literal: true

class V1::BaseController < ApplicationController
	def index
		books = Book.all
		render json: { boosk: books }, status: :ok
	end 
end
