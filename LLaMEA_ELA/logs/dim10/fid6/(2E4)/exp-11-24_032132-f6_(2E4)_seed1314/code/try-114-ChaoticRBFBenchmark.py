import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time_phase = 0.0
        self.amplitude_scale = 1.5
        self.frequency_mod = 2.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying phase for dynamic behavior
        self.time_phase = (self.time_phase + 0.01) % (2 * np.pi)
        
        # Radial Basis Function component with chaotic modulation
        rbf_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic radial basis with time-varying parameters
            sigma = 0.5 + 0.3 * np.sin(self.time_phase + i * 0.7)
            mu = 1.2 * np.cos(self.time_phase + i * 0.5)
            rbf_term += np.exp(-0.5 * ((xi - mu) / sigma)**2) * (1.0 + 0.3 * np.sin(xi * self.frequency_mod))
        
        # Multi-frequency sinusoidal modulation with dynamic coupling
        sin_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sinusoidal components with varying frequencies and amplitudes
            sin_term += (np.sin(xi * 2.1 + self.time_phase) * np.cos(xi * 1.3 + self.time_phase * 0.7) * 
                        np.exp(-0.1 * xi**2) +
                        np.sin(xi * 4.7 + self.time_phase * 1.3) * np.cos(xi * 3.2 + self.time_phase * 0.9) * 
                        np.exp(-0.05 * xi**2) +
                        np.sin(xi * 6.8 + self.time_phase * 1.7) * np.cos(xi * 5.4 + self.time_phase * 1.1) * 
                        np.exp(-0.02 * xi**2))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with time-varying coupling strength
                coupling_strength = 0.8 + 0.4 * np.sin(self.time_phase + i + j)
                cross_term += coupling_strength * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric polynomial with chaotic perturbations
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric polynomial with time-varying coefficients
            a = 1.0 + 0.2 * np.sin(self.time_phase + i)
            b = 0.8 + 0.3 * np.cos(self.time_phase + i)
            poly_term += (a * xi**4 + b * xi**3 - 0.5 * xi**2) * np.exp(-0.1 * xi**2)
        
        # Enhanced chaotic modulation with higher-order interactions
        enhanced_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Higher-order chaotic polynomial with dynamic exponents
            exponent = 3.0 + 1.5 * np.sin(self.time_phase + i * 1.2)
            coefficient = 0.5 + 0.3 * np.cos(self.time_phase + i * 0.8)
            enhanced_term += coefficient * (xi**exponent) * np.exp(-0.05 * xi**2)
        
        # Additional chaotic coupling between all dimensions
        global_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 0.6 + 0.4 * np.sin(self.time_phase * 1.3 + i * 0.5 + j * 0.3)
                    global_coupling += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all terms with time-varying weights
        weight_rbf = 0.7 + 0.3 * np.sin(self.time_phase)
        weight_sin = 0.8 + 0.2 * np.cos(self.time_phase)
        weight_cross = 0.6 + 0.4 * np.sin(self.time_phase * 1.5)
        weight_poly = 0.9 + 0.1 * np.cos(self.time_phase * 0.7)
        weight_enhanced = 0.5 + 0.5 * np.sin(self.time_phase * 2.0)
        weight_global = 0.4 + 0.6 * np.cos(self.time_phase * 1.2)
        
        return (weight_rbf * rbf_term + 
                weight_sin * sin_term + 
                weight_cross * cross_term + 
                weight_poly * poly_term +
                weight_enhanced * enhanced_term +
                weight_global * global_coupling)