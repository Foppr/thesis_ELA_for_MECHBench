import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic scaling factors for multi-scale modulation
        self.scaling_factors = [np.sin(i * 0.5 + 1) * np.sqrt(i + 1) for i in range(dim)]
        # Asymmetric coupling coefficients for directional bias
        self.coupling_coeffs = [np.tan(i * 0.3 + 0.1) * (i + 1) for i in range(dim)]
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic harmonic gradient components with varying scales
        gradient_sum = 0.0
        for i in range(self.dim):
            scaled_x = x_norm[i] * self.scaling_factors[i % len(self.scaling_factors)]
            # Multi-frequency chaotic modulation
            gradient_sum += (np.sin(scaled_x * 2.3) + 
                           0.7 * np.sin(scaled_x * 5.1) + 
                           0.3 * np.sin(scaled_x * 8.7)) * \
                          np.cos(scaled_x * 1.2)
        
        # Fractal-like curvature with asymmetric saddle points
        fractal_curvature = 0.0
        for i in range(self.dim):
            x_i = x_norm[i]
            # Asymmetric cubic and quartic terms
            fractal_curvature += (x_i**3 * np.cos(i * 0.8) + 
                                0.5 * x_i**4 * np.sin(i * 0.6)) * \
                               (1 + 0.2 * np.sin(i * 1.5))
        
        # Multi-scale coupling with perturbed exponential decay
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                diff = x_norm[i] - x_norm[j]
                # Perturbed coupling with directional weighting
                weight = (self.coupling_coeffs[i % len(self.coupling_coeffs)] + 
                         self.coupling_coeffs[j % len(self.coupling_coeffs)]) / 2.0
                coupling_term += diff**2 * np.exp(-abs(diff) * 0.5) * weight
        
        # Asymmetric peak attraction with harmonic phase shifts
        peak_attraction = 0.0
        for i in range(self.dim):
            # Create asymmetric peaks with chaotic positioning
            peak_pos = (np.sin(i * 0.7 + 0.2) * 0.5 + 
                       0.3 * np.cos(i * 1.1)) * 0.8
            dist_from_peak = abs(x_norm[i] - peak_pos)
            # Asymmetric exponential attraction
            peak_attraction += (np.exp(-dist_from_peak**2 * 2.0) * 
                              (1 + 0.3 * np.sin(i * 0.9)))
        
        # Enhanced conditioning through mixed polynomial terms with chaotic exponents
        conditioning = 0.0
        for i in range(self.dim):
            # Chaotic exponent modulation
            exp_mod = 2.0 + 0.5 * np.sin(i * 0.4)
            conditioning += x_norm[i]**exp_mod
        
        # Multi-modal component with chaotic frequency spectrum
        multimodal = 0.0
        for i in range(self.dim):
            # Multi-frequency sinusoidal modulation
            freq = 1.0 + 0.3 * np.sin(i * 0.8)
            multimodal += np.sin(freq * x_norm[i] * 3.2) * np.cos(freq * x_norm[i] * 2.1)
        
        # Combine all components with dynamic weights
        result = 0.25 * gradient_sum + 0.20 * fractal_curvature + \
                 0.25 * coupling_term + 0.15 * peak_attraction + \
                 0.10 * conditioning + 0.05 * multimodal
        
        return result