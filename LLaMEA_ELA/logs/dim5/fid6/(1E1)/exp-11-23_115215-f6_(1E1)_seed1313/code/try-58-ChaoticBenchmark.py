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
            
        # Add quantum-inspired radial basis function components with phase modulation
        for i in range(self.dim):
            # Quantum-like RBF with dynamic center, width, and phase
            center = np.sin(i * 0.7) * 4.0
            width = 0.3 + 0.7 * np.cos(i * 0.4)
            phase = np.sin(i * 0.9)
            f_val += 0.25 * np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(phase * x[i])
            
        # Add hypercomplex coupling terms with multi-dimensional interaction
        for i in range(self.dim):
            if i > 0:
                # Hypercomplex interaction: multidirectional influence with different weights
                f_val += 0.2 * (x[i] - x[i-1])**4 + 0.15 * np.abs(x[i] - x[i-1])**2.5 + \
                         0.05 * np.sin(x[i] + x[i-1]) * np.cos(x[i] - x[i-1])
                
        # Add multi-scale sinusoidal modulations with complex frequency interactions
        for i in range(self.dim):
            f_val += 0.3 * np.sin(3 * x[i]) * np.cos(4 * x[i]) + \
                     0.15 * np.sin(7 * x[i]) * np.cos(9 * x[i]) + \
                     0.08 * np.sin(13 * x[i]) * np.cos(17 * x[i]) + \
                     0.03 * np.sin(23 * x[i])
                     
        # Add polynomial coupling with logarithmic weights and cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.log(1 + 0.5 * (i + j))
                f_val += weight * (x[i]**3) * (x[j]**2) + 0.1 * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Add chaotic phase coupling with multi-delayed terms
        for i in range(self.dim):
            if i > 2:
                delayed_term = np.sin(x[i-3] + 0.3 * x[i-2] + 0.7 * x[i-1])
                f_val += 0.15 * delayed_term * np.cos(2 * x[i])
                
        # Add a final hypercomplex non-linear transformation
        f_val += 0.15 * np.sin(np.sum(x**4)) + 0.1 * np.cos(np.prod(x)) + \
                 0.05 * np.tanh(np.sum(x**3))
        
        return f_val