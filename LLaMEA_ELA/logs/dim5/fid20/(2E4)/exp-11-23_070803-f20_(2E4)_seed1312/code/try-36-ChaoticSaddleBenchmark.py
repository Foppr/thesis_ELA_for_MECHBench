import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic saddle point component with sinusoidal modulation
        chaotic_term = 0
        for i in range(self.dim):
            chaotic_term += np.sin(12 * x_norm[i]) * np.cos(10 * x_norm[i]) + \
                           np.sin(18 * x_norm[i]**2) * np.cos(15 * x_norm[i]**2)
        
        # Embedded Gaussian mixture components with varying covariances
        gaussian_term = 0
        gaussians = [
            (np.array([0.6, -0.4, 0.9]), np.array([[0.6, 0.15], [0.15, 0.35]])),
            (np.array([-0.8, 0.5, -0.7]), np.array([[0.25, -0.15], [-0.15, 0.45]])),
            (np.array([0.3, 1.0, -0.6]), np.array([[0.35, 0.05], [0.05, 0.25]]))
        ]
        
        # Only process first 3 dimensions if dim >= 3, otherwise use available dims
        for i in range(min(3, self.dim)):
            x_i = x_norm[i:i+1] if i < self.dim-1 else np.array([x_norm[i]])
            mean = np.array(gaussians[i][0][:len(x_i)])
            cov = gaussians[i][1][:len(x_i), :len(x_i)]
            
            # Multivariate Gaussian
            diff = x_i - mean
            gaussian_term += np.exp(-0.5 * np.dot(np.dot(diff, np.linalg.inv(cov)), diff.T))
        
        # Polynomial decay barriers with varying exponents
        barrier_term = 0
        for i in range(self.dim):
            barrier_term += (1 + 0.6 * x_norm[i]**2) ** (-4) + \
                          (1 + 0.4 * np.abs(x_norm[i])) ** (-3)
        
        # Cross-term coupling with exponential decay
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.15)
                cross_term += np.exp(-dist) * np.sin(7 * (x_norm[i] + x_norm[j]))
        
        # Combined function with scaling factors
        result = 2.5 * chaotic_term + 0.6 * gaussian_term + 2.0 * barrier_term + 1.0 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise