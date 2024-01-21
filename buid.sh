echo "Usage: run in the project dir!"
pwd;

cd frontend/
npm run build

sed -i 's#/assets/#/static/assets/#' dist/index.html
# cp file to py server
cp dist/assets/* ../backend/static/assets/
cp dist/index.html ../backend/templates/dist/

echo "done!"