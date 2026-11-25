import numpy as np

class ChaoticRBFHypersineBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component with dynamic parameter modulation
        chaotic = 0.0
        r_param = 3.9 + 0.1 * np.sin(0.5 * np.sum(x))
        for i in range(self.dim):
            x_prev = x[i] if i == 0 else x[i-1]
            chaotic += np.log(1.0 + np.abs(r_param * x_prev * (1.0 - x_prev)))
        
        # Radial basis function with dynamic centers and widths
        rbf = 0.0
        num_centers = min(5, self.dim)
        for i in range(num_centers):
            center = -4.0 + 8.0 * (i / (num_centers - 1) if num_centers > 1 else 0.5)
            width = 0.5 + 0.3 * np.sin(0.3 * center)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Asymmetric hyperbolic sine coupling
        hyperbolic = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                diff = x[i] - x[j]
                hyperbolic += np.sinh(diff) * np.cosh(0.5 * diff)
        
        # Polynomial cross-dimensional coupling with dynamic exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                exp_i = 2.0 + 0.5 * np.sin(0.4 * x[i])
                exp_j = 2.0 + 0.5 * np.cos(0.4 * x[j])
                poly_coupling += (x[i]**exp_i + x[j]**exp_j) * np.sin(0.3 * (x[i] + x[j]))
        
        # Multi-scale harmonic potential with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.2 * x[i])
            amp_mod = 1.0 + 0.3 * np.cos(0.1 * x[i])
            harmonic += amp_mod * np.sin(freq_mod * x[i] + 0.1 * np.sin(5.0 * x[i]))
        
        # Memory-dependent gradient structure
        memory = 0.0
        for i in range(self.dim):
            if i > 0:
                memory += 0.2 * (x[i] - x[i-1])**3 + 0.1 * np.sin(0.5 * (x[i] + x[i-1]))
        
        # Combine all components with dimensionally adaptive weights
        total = (0.25 * chaotic + 0.20 * rbf + 0.15 * hyperbolic + 
                0.20 * poly_coupling + 0.15 * harmonic + 0.05 * memory)
        
        # Normalize by dimension
        return total / np.sqrt(self.dim)