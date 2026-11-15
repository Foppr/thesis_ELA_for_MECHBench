import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying exponents
        polynomial = np.sum(x**4 + 0.5 * x**3 + 0.1 * x**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        trigonometric = 0
        for i in range(self.dim):
            trigonometric += (np.sin(2 * x[i]) * np.cos(3 * x[i]) * 
                             np.exp(-0.1 * np.abs(x[i])) * 
                             np.sin(0.5 * x[i]**2))
        
        # Asymmetric cross-terms with different interaction strengths
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction: different coefficients for i and j
                cross += 0.3 * x[i] * x[j] * np.sin(0.2 * x[i]) * np.cos(0.3 * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Logarithmic perturbations with adaptive scaling
        log_perturbation = 0
        for i in range(self.dim):
            log_perturbation += np.log(1 + 0.5 * x[i]**2) * np.sin(0.4 * x[i]) * np.cos(0.1 * x[i]**3)
        
        # Saddle point structure with varying curvature
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 2 * x[i]**4 + x[i]**2) * np.exp(-0.01 * x[i]**2)
        
        # Adaptive conditioning based on dimension
        conditioning = 0
        for i in range(self.dim):
            conditioning += 0.01 * i * np.sin(x[i]) * np.cos(x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Mixed chaotic and periodic interference
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interference += 0.2 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(2 * x[i] - x[j]) * (x[i]**2 + x[j]**2)
        
        return polynomial + trigonometric + cross + log_perturbation + saddle + conditioning + interference