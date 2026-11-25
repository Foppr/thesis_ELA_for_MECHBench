import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute tent map parameters for enhanced chaos
        self.a_values = np.linspace(1.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic tent map components
        for i in range(self.dim):
            # Tent map with parameter a_i
            if i == 0:
                tent_val = x[i]
            else:
                tent_val = self.a_values[i] * np.abs(x[i-1] - 0.5)
            f_val += 0.4 * np.sin(tent_val * 15) * np.cos(tent_val * 11)
            
        # Add quantum-like interference patterns with complex amplitudes
        for i in range(self.dim):
            # Complex interference with dynamic phase
            phase = np.sin(i * 0.7) * np.pi
            amplitude = 0.3 + 0.2 * np.cos(i * 0.4)
            f_val += amplitude * np.sin(x[i] * 8 + phase) * np.cos(x[i] * 5 + phase)
            
        # Add spatio-temporal coupling with memory effects
        for i in range(self.dim):
            if i > 0:
                # Memory-based interaction: influence from previous two dimensions
                f_val += 0.2 * (x[i] - x[i-1])**4 + 0.15 * np.abs(x[i] - x[i-1])**2.5
                
        # Add multi-scale wavelet-like modulations
        for i in range(self.dim):
            f_val += 0.3 * np.sin(3 * x[i]) * np.cos(4 * x[i]) + \
                     0.15 * np.sin(7 * x[i]) * np.cos(9 * x[i]) + \
                     0.08 * np.sin(13 * x[i])
                     
        # Add polynomial coupling with logarithmic weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + np.log(1.0 + i + j))
                f_val += weight * (x[i]**3) * (x[j]**2) + 0.1 * x[i] * x[j]
                
        # Add chaotic phase coupling with delayed feedback
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.tan(x[i-3] + 0.3 * x[i-2])
                f_val += 0.15 * delayed_term * np.sin(x[i])
                
        # Add a final complex non-linear transformation with hyperbolic components
        f_val += 0.12 * np.sinh(np.sum(x**4)) + 0.08 * np.cosh(np.prod(x))
        
        return f_val