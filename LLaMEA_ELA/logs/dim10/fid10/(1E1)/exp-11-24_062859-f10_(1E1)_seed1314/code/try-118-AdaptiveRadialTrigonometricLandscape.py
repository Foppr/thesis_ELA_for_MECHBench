import numpy as np

class AdaptiveRadialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial landscape with adaptive conditioning
        result = 0.01 * np.sum(x**4) + 0.5 * np.sum(x**2)
        
        # Radial basis function components with varying widths
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.1 * (x[i] - 2)**2) + 1.5 * np.exp(-0.2 * (x[i] + 3)**2)
        
        # Multi-scale trigonometric interference with frequency modulation
        for i in range(self.dim):
            result += 1.2 * np.sin(3 * x[i]) * np.cos(5 * x[i]) + 0.8 * np.sin(7 * x[i])
            
        # Asymmetric polynomial terms with cross-dimensional coupling
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.6 * x[i]**3.5
            else:
                result += 0.3 * x[i]**4.2
                
        # Cross-dimensional interaction with distance-dependent weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.5 * np.exp(-dist) * np.sin(2 * (x[i] + x[j]))
        
        # Adaptive conditioning with spatially varying exponents
        for i in range(self.dim):
            result += 0.4 * np.abs(x[i])**1.8 * (1 + 0.3 * np.sin(0.5 * x[i]))
            
        # High-frequency oscillation with amplitude modulation
        for i in range(self.dim):
            result += 1.8 * np.sin(12 * x[i]) * np.cos(9 * x[i]) * (1 + 0.2 * np.tanh(x[i]))
        
        # Add small random noise to prevent trivial convergence
        result += 0.01 * np.random.random()
        
        return result