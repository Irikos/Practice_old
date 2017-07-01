class Comment < ActiveRecord::Base
  belongs_to :article
  validates :name, presence: true
  validates :body, presence: true
end
