import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic tent map dynamics for enhanced complexity
        chaotic_term = 0.0
        for i in range(self.dim):
            # Tent map with parameter that creates chaos
            a = 1.8 + 0.2 * np.sin(0.5 * i)
            if x_norm[i] < 0.5:
                tent_val = a * x_norm[i]
            else:
                tent_val = a * (1 - x_norm[i])
            chaotic_term += tent_val**3
        
        # Enhanced polynomial with multiple roots and varying exponents
        poly_term = 0.0
        exponents = [2, 3, 4, 5, 6]
        for i in range(self.dim):
            exp_idx = i % len(exponents)
            poly_term += (x_norm[i]**exponents[exp_idx]) * np.cos(2 * np.pi * x_norm[i])
        
        # Trigonometric terms with varying frequencies and amplitudes
        trig_term = 0.0
        freqs = [1, 3, 5, 7, 9]
        for i in range(self.dim):
            freq_idx = i % len(freqs)
            trig_term += np.sin(freqs[freq_idx] * x_norm[i])**2 + \
                        np.cos(freqs[freq_idx] * x_norm[i]) * np.sin(0.5 * freqs[freq_idx] * x_norm[i])
        
        # Radial basis function component with asymmetric and dynamic centers
        rbf_term = 0.0
        for i in range(self.dim):
            center1 = 0.3 * np.sin(0.7 * i) + 0.2
            center2 = -0.3 * np.cos(0.6 * i) - 0.1
            sigma1 = 0.5 + 0.2 * np.sin(0.8 * i)
            sigma2 = 0.4 + 0.1 * np.cos(0.9 * i)
            rbf_term += np.exp(-sigma1 * (x_norm[i] - center1)**2) + \
                       0.7 * np.exp(-sigma2 * (x_norm[i] - center2)**2)
        
        # Cross-dimensional coupling with chaotic interaction strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Chaotic interaction strength based on both dimensions
                strength = 0.8 + 0.2 * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
                cross_term += strength * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j])
        
        # Asymmetric penalty term with chaotic modulation
        asym_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation of asymmetry
            mod = 1 + 0.5 * np.sin(2 * np.pi * i / self.dim)
            asym_term += mod * ((x_norm[i] - 0.1)**3 + 0.3 * (x_norm[i] + 0.2)**2)
        
        # Combine all terms with dynamic weights
        weights = [0.7 + 0.1 * np.sin(0.5 * i) for i in range(self.dim)]
        result = 0.6 * chaotic_term + 0.5 * poly_term + 0.4 * trig_term + \
                0.3 * rbf_term + 0.2 * cross_term + 0.1 * asym_term
        
        return result