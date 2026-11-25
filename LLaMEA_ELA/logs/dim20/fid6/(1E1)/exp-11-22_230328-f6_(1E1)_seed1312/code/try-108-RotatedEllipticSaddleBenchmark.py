import numpy as np

class RotatedEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
        # Adaptive condition numbers for different subspaces
        self.condition_numbers = np.logspace(0, 3, dim//2 + 1) if dim > 1 else [1.0]
        
        # Saddle point cluster locations and strengths
        self.saddle_clusters = []
        num_clusters = max(1, dim // 4)
        for _ in range(num_clusters):
            center = np.random.uniform(-3, 3, dim)
            strength = np.random.uniform(0.5, 2.0)
            self.saddle_clusters.append((center, strength))
    
    def f(self, x):
        # Apply rotation
        x_rot = self.rotation_matrix @ x
        
        # Elliptic term with adaptive condition number
        elliptic_term = 0.0
        for i in range(self.dim):
            cond_num = self.condition_numbers[i % len(self.condition_numbers)]
            elliptic_term += cond_num * (x_rot[i] ** 2)
        
        # Saddle point terms
        saddle_term = 0.0
        for center, strength in self.saddle_clusters:
            # Dynamic shift based on input
            shift = np.sin(0.5 * x) * 0.5
            dist = np.linalg.norm(x_rot - (center + shift))
            saddle_term += strength * np.exp(-dist**2 / 2.0)
        
        # Add noise that depends on position
        noise = np.sum(np.sin(x_rot) * np.cos(x_rot) * 0.01)
        
        return elliptic_term - saddle_term + noise