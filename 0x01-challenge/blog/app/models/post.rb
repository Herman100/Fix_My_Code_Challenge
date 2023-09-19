class Post < ApplicationRecord
  has_many  :comments, dependent: :destroy
  validates :title, presence: true, length: {minimum: 5}
	validates :body,  presence: true

  def post_params
    params.require(:post).permit(:title, :body, :online)

end
