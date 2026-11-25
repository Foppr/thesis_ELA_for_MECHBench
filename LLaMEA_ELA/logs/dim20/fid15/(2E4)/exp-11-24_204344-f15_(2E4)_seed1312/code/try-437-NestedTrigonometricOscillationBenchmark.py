import numpy as np

class NestedTrigonometricOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for nested trigonometric components
        self.frequency_scales = np.random.uniform(0.5, 5.0, dim)
        self.amplitude_scales = np.random.uniform(0.1, 3.0, dim)
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        self.polynomial_chaos_coeffs = np.random.randn(dim, 6)
        self.nested_depth = np.random.randint(2, 6, dim)
        self.symmetry_breakers = np.random.uniform(-0.5, 0.5, dim)
        self.global_scaling = np.random.uniform(0.5, 2.0)
        
    def f(self, x):
        x = np.array(x)
        result = 0.0
        
        # Nested trigonometric oscillation component
        for i in range(self.dim):
            freq_scale = self.frequency_scales[i]
            amp_scale = self.amplitude_scales[i]
            phase_shift = self.phase_shifts[i]
            
            # Build nested oscillations with increasing complexity
            nested_value = 0.0
            for depth in range(1, self.nested_depth[i] + 1):
                nested_value += amp_scale * np.sin(freq_scale * x[i] ** depth + phase_shift)
                
            result += nested_value
            
        # Polynomial chaos expansion for symmetry breaking
        chaos_term = 0.0
        for i in range(self.dim):
            coeffs = self.polynomial_chaos_coeffs[i]
            poly_value = (coeffs[0] * x[i] +
                         coeffs[1] * x[i]**2 +
                         coeffs[2] * x[i]**3 +
                         coeffs[3] * x[i]**4 +
                         coeffs[4] * x[i]**5 +
                         coeffs[5] * x[i]**6)
            chaos_term += poly_value
            
        # Symmetry breaking component
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += self.symmetry_breakers[i] * np.sin(x[i] * np.cos(x[i]))
            
        # Global scaling and fitness adjustment
        global_factor = self.global_scaling * (1.0 + 0.1 * np.sin(np.sum(x) * 0.5))
        
        # Combine all terms with adaptive weighting
        total = 0.4 * result + 0.3 * chaos_term + 0.2 * symmetry_term
        
        return global_factor * total + 0.01 * np.sum(x**2)