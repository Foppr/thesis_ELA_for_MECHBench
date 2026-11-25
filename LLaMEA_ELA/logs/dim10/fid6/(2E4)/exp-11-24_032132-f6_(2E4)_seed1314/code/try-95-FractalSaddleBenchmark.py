import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 0.7
        self.saddle_strength = 3.2
        self.coupling_strength = 2.5
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial term with non-integer exponents and chaotic modulation
        fractal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            exponent = 2.3 + self.fractal_dim * np.sin(xi * 1.5 + i * 0.7)
            fractal_term += np.abs(xi)**exponent
        
        # Asymmetric saddle points with varying heights, widths, and chaotic phase shifts
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic phase shift based on position
            phase_shift = np.sin(xi * 0.8 + i * 0.3)
            if xi >= 0:
                saddle_term += self.saddle_strength * (xi**5 - 3*xi**3 + xi) * np.exp(-0.1 * xi**2) * (1 + 0.2 * phase_shift)
            else:
                saddle_term += self.saddle_strength * (xi**4 - 2*xi**2) * np.exp(-0.05 * xi**2) * (1 + 0.15 * phase_shift)
        
        # Dynamic coupling between dimensions with chaotic phase shifts and higher-order interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic phase based on both indices and values
                phase = np.sin(0.7 * (i + j) + x[i] * 0.3 + x[j] * 0.2)
                coupling_term += self.coupling_strength * np.sin(x[i] + x[j] + phase) * \
                                (x[i]**3 + x[j]**3) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        
        # Multi-scale sinusoidal modulation with higher frequencies and chaotic amplitude variations
        mod_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Higher frequency components with chaotic amplitudes
            amp1 = 1.2 + 0.3 * np.sin(xi * 2.1 + i * 0.5)
            amp2 = 0.8 + 0.2 * np.cos(xi * 3.7 + i * 0.8)
            amp3 = 0.6 + 0.1 * np.sin(xi * 5.3 + i * 1.2)
            
            mod_term += (amp1 * np.sin(xi * 4.1) * np.cos(xi * 2.3) * np.exp(-0.15 * xi**2) + 
                        amp2 * np.sin(xi * 6.7) * np.cos(xi * 3.8) * np.exp(-0.1 * xi**2) +
                        amp3 * np.sin(xi * 8.9) * np.cos(xi * 5.4) * np.exp(-0.05 * xi**2))
        
        # Asymmetric radial component with chaotic conditioning and higher-order terms
        radial_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Radial term with chaotic behavior based on sign of dimension
            if xi >= 0:
                radial_term += (xi**4 + 0.7*xi**3 + 0.2*xi**2) * np.exp(-0.2 * xi**2)
            else:
                radial_term += (xi**5 - 0.4*xi**4 + 0.1*xi**3) * np.exp(-0.15 * xi**2)
        
        # Combine all terms with enhanced scaling
        return 0.8 * fractal_term + 1.5 * saddle_term + 1.2 * coupling_term + 0.9 * mod_term + 0.7 * radial_term