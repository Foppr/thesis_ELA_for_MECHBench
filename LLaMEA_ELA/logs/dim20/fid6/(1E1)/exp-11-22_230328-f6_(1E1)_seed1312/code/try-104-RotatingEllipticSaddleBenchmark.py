import numpy as np

class RotatingEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation angles for each dimension pair
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim//2 + dim%2)
        # Set condition numbers for each dimension (higher values = more ill-conditioned)
        self.condition_numbers = np.random.uniform(10, 1000, dim)
        # Saddle point cluster locations and strengths
        self.saddle_clusters = []
        num_clusters = max(1, dim // 3)
        for _ in range(num_clusters):
            center = np.random.uniform(-3, 3, dim)
            strength = np.random.uniform(0.5, 2.0)
            self.saddle_clusters.append((center, strength))
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Apply rotation to the input vector
        if self.dim % 2 == 0:
            rotated = x_norm.copy()
            for i in range(0, self.dim, 2):
                angle = self.rotation_angles[i//2]
                cos_a, sin_a = np.cos(angle), np.sin(angle)
                rotated[i], rotated[i+1] = (
                    cos_a * x_norm[i] - sin_a * x_norm[i+1],
                    sin_a * x_norm[i] + cos_a * x_norm[i+1]
                )
        else:
            rotated = x_norm.copy()
            for i in range(0, self.dim-1, 2):
                angle = self.rotation_angles[i//2]
                cos_a, sin_a = np.cos(angle), np.sin(angle)
                rotated[i], rotated[i+1] = (
                    cos_a * x_norm[i] - sin_a * x_norm[i+1],
                    sin_a * x_norm[i] + cos_a * x_norm[i+1]
                )
        
        # Elliptic term with adaptive condition number
        elliptic_term = 0.0
        for i in range(self.dim):
            elliptic_term += self.condition_numbers[i] * (rotated[i] ** 2)
        
        # Saddle point clusters
        saddle_term = 0.0
        for center, strength in self.saddle_clusters:
            dist = np.sum((rotated - center) ** 2)
            saddle_term += strength * np.exp(-dist / 2.0) * np.cos(dist)
        
        # Adaptive difficulty modifier based on input magnitude
        adaptive_factor = 1.0 + 0.5 * np.tanh(np.sum(np.abs(rotated)) - 1.0)
        
        # Combine terms with dynamic scaling
        total = elliptic_term + saddle_term * adaptive_factor
        
        return total