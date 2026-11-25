import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for enhanced complexity
        self.r_values = np.linspace(3.8, 4.0, dim)
        self.phase_shifts = np.linspace(0, 2*np.pi, dim)
        self.memory_weights = np.exp(-np.arange(dim) * 0.1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = np.sum(x**2) * (1 + 0.1 * np.sin(np.sum(x)))
        
        # Nested chaotic logistic maps with memory effects
        chaotic_vals = np.zeros(self.dim)
        for i in range(self.dim):
            if i == 0:
                chaotic_vals[i] = x[i]
            else:
                chaotic_vals[i] = self.r_values[i] * chaotic_vals[i-1] * (1 - chaotic_vals[i-1])
            f_val += 0.5 * np.sin(chaotic_vals[i] * 15) * np.cos(chaotic_vals[i] * 11)
            
        # Quantum-like interference terms with phase modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                interference = np.sin(distance * 10 + self.phase_shifts[i]) * np.cos(distance * 7 + self.phase_shifts[j])
                f_val += 0.3 * interference / (1 + distance**2)
                
        # Memory-dependent couplings with time-delayed chaotic feedback
        for i in range(self.dim):
            if i > 2:
                memory_contribution = self.memory_weights[i-1] * np.sin(x[i-2] + 0.3 * x[i-1])
                f_val += 0.2 * memory_contribution * np.cos(x[i])
                
        # Multi-scale radial basis functions with dynamic centers and varying kernel widths
        for i in range(self.dim):
            center = 3.0 * np.sin(i * 0.7 + np.sum(x) * 0.1)
            width = 0.3 + 0.7 * np.cos(i * 0.4 + np.sum(x) * 0.2)
            f_val += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**4)
            
        # Asymmetric polynomial couplings with exponential weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = np.exp(-0.2 * (j-i)) * np.cos(x[i]) * np.sin(x[j])
                f_val += weight * (x[i]**3) * (x[j]**2) + 0.1 * x[i] * x[j]
                
        # Fractional-order chaotic dynamics with Hurst exponent modulation
        for i in range(self.dim):
            if i > 0:
                fractional_diff = np.abs(x[i] - x[i-1]) ** 0.7
                f_val += 0.25 * fractional_diff * np.sin(x[i] * 5)
                
        # Nested sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq_factor = 1 + 0.5 * np.sin(i * 0.3)
            f_val += 0.3 * np.sin(freq_factor * x[i] * 8) * np.cos(freq_factor * x[i] * 6) + \
                     0.15 * np.sin(freq_factor * x[i] * 12) * np.cos(freq_factor * x[i] * 9)
                     
        # Add a complex non-linear transformation with multiple transcendental components
        sum_x_cubed = np.sum(x**3)
        prod_x = np.prod(x)
        f_val += 0.2 * np.sin(sum_x_cubed) * np.cos(prod_x) + \
                 0.1 * np.exp(-np.abs(sum_x_cubed)) * np.log(1 + np.abs(prod_x))
        
        return f_val