import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map sequence for chaos
        self.logistic_seq = np.array([0.5])
        for i in range(dim * 20):
            self.logistic_seq = np.append(self.logistic_seq, 4 * self.logistic_seq[-1] * (1 - self.logistic_seq[-1]))
        self.logistic_seq = self.logistic_seq[:dim]
        
        # Fractal scaling parameters
        self.fractal_scale = np.random.uniform(0.1, 2.0, dim)
        
        # Saddle point structure
        self.saddle_points = np.random.uniform(-5.0, 5.0, (3, dim))
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - self.logistic_seq[i])**2) / (2 * (0.1 * self.fractal_scale[i])**2))
        
        # Logistic map chaotic dynamics
        chaotic = np.sum(self.logistic_seq * np.sin(2 * np.pi * x_norm))
        
        # Asymmetric noise component
        noise = np.sum(np.abs(x_norm) * np.random.uniform(0.5, 1.5, self.dim))
        
        # Polynomial interaction with mixed degrees
        poly_interaction = np.sum(x_norm**3) + 0.5 * np.sum(x_norm**5) + 0.1 * np.sum(x_norm**7)
        
        # Fractal scaling component
        fractal = np.sum(np.sin(self.fractal_scale * x_norm) * np.cos(self.fractal_scale * x_norm))
        
        # Saddle point attraction/repulsion
        saddle = 0
        for point in self.saddle_points:
            dist = np.sum((x - point)**2)
            saddle += 1.0 / (1.0 + dist)
        
        # Combine components with varying weights
        return 0.2 * np.sum(rbfs) + 0.3 * chaotic + 0.2 * noise + 0.15 * poly_interaction + 0.1 * fractal + 0.05 * saddle