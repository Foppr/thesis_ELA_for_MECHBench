import numpy as np

class AdaptiveRotatedQuadraticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrices for each dimension
        self.rotation_matrices = []
        for _ in range(dim):
            # Create random orthogonal matrix
            A = np.random.randn(dim, dim)
            Q, _ = np.linalg.qr(A)
            self.rotation_matrices.append(Q)
        
        # Adaptive conditioning parameters
        self.conditioning = np.random.uniform(1.0, 100.0, dim)
        
        # Multiplier for trigonometric components
        self.trig_multiplier = np.random.uniform(0.5, 2.0, dim)
        
        # Local minima positions
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 3))
        
        # Dynamic weights for combining components
        self.weights = np.random.uniform(0.1, 1.0, 4)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Quadratic component with conditioning
        quadratic_term = 0.0
        for i in range(self.dim):
            transformed_x = np.dot(self.rotation_matrices[i], x)
            quadratic_term += self.conditioning[i] * transformed_x[i]**2
            
        # Trigonometric component
        trig_term = 0.0
        for i in range(self.dim):
            transformed_x = np.dot(self.rotation_matrices[i], x)
            trig_term += self.trig_multiplier[i] * np.sin(transformed_x[i]) * np.cos(transformed_x[i])
            
        # Multimodal component with local minima attraction
        multimodal_term = 0.0
        for i in range(self.dim):
            distances = np.abs(x[i] - self.minima_positions[i, :])
            min_dist = np.min(distances)
            multimodal_term += min_dist ** 2
            
        # Cross-dimensional interaction term
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] - x[j])**2
                
        # Combine all components with adaptive weights
        total = (self.weights[0] * quadratic_term + 
                 self.weights[1] * trig_term + 
                 self.weights[2] * multimodal_term + 
                 self.weights[3] * cross_term)
        
        return total