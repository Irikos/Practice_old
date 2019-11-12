class WelcomeController < ApplicationController

  @hello = ""
  def index
    @hello = "Hello, world!"
  end

  def hello
    @hello = "Hello, name!"
  end
end
