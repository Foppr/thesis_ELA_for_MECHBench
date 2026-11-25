import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 0.42
        self.saddle_strength = 3.1
        self.coupling_strength = 2.7
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like polynomial term with non-integer exponents and enhanced chaos
        fractal_term = np.sum(np.abs(x)**(2.9 + self.fractal_dim * np.sin(x[0] if len(x) > 0 else 0) + 
                                         0.3 * np.cos(x[1] if len(x) > 1 else 0))) * 0.15
        
        # Asymmetric saddle points with varying heights, widths, and chaotic modulation
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create asymmetric saddle with different curvature on each side and chaotic modulation
            if xi >= 0:
                saddle_term += self.saddle_strength * (xi**4 - 2*xi**2 + 0.3*np.sin(5*xi)) * np.exp(-0.15 * xi**2)
            else:
                saddle_term += self.saddle_strength * (xi**3 - xi + 0.2*np.cos(7*xi)) * np.exp(-0.08 * xi**2)
        
        # Dynamic coupling between dimensions with phase shifts and chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling with varying strength, phase, and chaotic modulation
                phase = np.sin(0.7 * (i + j) + 0.5 * np.cos(i*j))
                coupling_term += self.coupling_strength * np.sin(x[i] + x[j] + phase) * \
                                (x[i]**2 + x[j]**2 + 0.4*np.sin(x[i]*x[j])) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        
        # Multi-scale sinusoidal modulation with varying frequencies, amplitudes, and chaotic components
        mod_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency components with different amplitudes and chaotic modulation
            mod_term += (np.sin(xi * 4.2) * np.cos(xi * 2.1) * np.exp(-0.25 * xi**2) + 
                        np.sin(xi * 6.8) * np.cos(xi * 3.7) * np.exp(-0.15 * xi**2) +
                        np.sin(xi * 9.1) * np.cos(xi * 5.2) * np.exp(-0.08 * xi**2) +
                        0.3 * np.sin(12*xi) * np.cos(8*xi) * np.exp(-0.05 * xi**2))
        
        # Asymmetric radial component with dynamic conditioning and chaotic perturbations
        radial_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Radial term with asymmetric behavior based on sign of dimension and chaotic perturbation
            if xi >= 0:
                radial_term += (xi**3 + 0.6*xi**2 + 0.2*np.sin(10*xi)) * np.exp(-0.2 * xi**2)
            else:
                radial_term += (xi**4 - 0.4*xi**3 + 0.15*np.cos(9*xi)) * np.exp(-0.15 * xi**2)
        
        # Combine all terms with proper scaling and enhanced chaotic behavior
        return 0.6 * fractal_term + 1.4 * saddle_term + 0.9 * coupling_term + 0.7 * mod_term + 0.5 * radial_term