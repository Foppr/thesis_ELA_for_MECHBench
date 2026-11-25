import numpy as np

class AdaptiveQuadraticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrices and condition numbers for each dimension
        self.rotation_matrices = []
        self.condition_numbers = []
        for _ in range(dim):
            # Create random orthogonal matrix
            A = np.random.randn(dim, dim)
            Q, _ = np.linalg.qr(A)
            self.rotation_matrices.append(Q)
            
            # Condition number between 10 and 1000
            cond_num = np.random.uniform(10, 1000)
            self.condition_numbers.append(cond_num)
        
        # Generate saddle point locations
        self.saddle_points = np.random.uniform(-5.0, 5.0, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation and condition number transformation
        total_value = 0.0
        for i in range(self.dim):
            # Rotate the vector
            rotated_x = self.rotation_matrices[i] @ x_norm
            
            # Apply quadratic form with adaptive condition number
            quad_form = np.sum((rotated_x ** 2) / self.condition_numbers[i])
            
            # Add saddle point influence
            saddle_influence = 0.0
            for j in range(self.dim):
                diff = rotated_x[j] - self.saddle_points[i, j]
                saddle_influence += diff ** 2 * np.sin(5 * diff)
            
            total_value += quad_form + 0.5 * saddle_influence
        
        # Add noise component
        noise = 0.01 * np.random.rand()
        
        return total_value + noise