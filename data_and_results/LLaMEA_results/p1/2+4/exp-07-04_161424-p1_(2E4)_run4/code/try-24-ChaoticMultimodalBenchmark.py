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
        self.fractal_scale = np.random.uniform(0.5, 3.0, dim)
        
        # Saddle point structure
        self.saddle_points = np.random.uniform(-5.0, 5.0, (3, dim))
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic scaling
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - self.logistic_seq[i])**2) / (2 * (0.15 * self.fractal_scale[i])**2))
        
        # Logistic map chaotic dynamics
        chaotic = np.sum(self.logistic_seq * np.sin(3 * np.pi * x_norm))
        
        # Asymmetric noise component
        noise = np.sum(np.abs(x_norm)**1.5 * np.random.uniform(0.3, 1.7, self.dim))
        
        # Polynomial interaction with mixed degrees (modified)
        poly_interaction = np.sum(x_norm**4) + 0.3 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8)
        
        # Fractal scaling component (enhanced)
        fractal = np.sum(np.sin(self.fractal_scale * x_norm**2) * np.cos(self.fractal_scale * x_norm**3))
        
        # Saddle point attraction/repulsion
        saddle = 0
        for point in self.saddle_points:
            dist = np.sum((x - point)**2)
            saddle += 1.0 / (1.0 + dist**1.5)
        
        # Combine components with new weights
        return 0.15 * np.sum(rbfs) + 0.35 * chaotic + 0.25 * noise + 0.1 * poly_interaction + 0.1 * fractal + 0.05 * saddle