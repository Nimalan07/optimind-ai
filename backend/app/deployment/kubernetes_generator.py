class KubernetesGenerator:

    @staticmethod
    def deployment():

        return """
apiVersion: apps/v1

kind: Deployment

metadata:
  name: ai-optimizer

spec:

  replicas: 1

  selector:

    matchLabels:

      app: ai-optimizer

  template:

    metadata:

      labels:

        app: ai-optimizer

    spec:

      containers:

      - name: optimizer

        image: ai-optimizer:latest

        ports:

        - containerPort: 8000
""".strip()

    @staticmethod
    def service():

        return """
apiVersion: v1

kind: Service

metadata:

  name: ai-optimizer-service

spec:

  selector:

    app: ai-optimizer

  ports:

  - port: 80

    targetPort: 8000

  type: LoadBalancer
""".strip()
