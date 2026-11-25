import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine-wave modulation parameters
        self.sin_freq = 3.0 + 4.0 * np.random.rand(dim)
        self.sin_amp = 1.5 + 2.5 * np.random.rand(dim)
        # Dynamic Gaussian peak parameters
        self.gauss_centers = np.random.uniform(-4.0, 4.0, (dim, 7))
        self.gauss_heights = 3.0 + 4.0 * np.random.rand(dim, 7)
        self.gauss_widths = 0.3 + 1.2 * np.random.rand(dim, 7)
        # Cross-dimensional cubic coupling coefficients
        self.cubic_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim, dim))
        # Time-varying conditioning factors with higher chaos
        self.time_factor = 1.5 + 0.5 * np.sin(0.15 * dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave modulation component
        sine_mod = 0.0
        for i in range(self.dim):
            mod_freq = self.sin_freq[i] * (1.0 + 0.3 * np.sin(0.4 * x[i] + 0.2 * i))
            mod_amp = self.sin_amp[i] * (1.0 + 0.2 * np.cos(0.5 * x[i] + 0.3 * i))
            sine_mod += mod_amp * np.sin(mod_freq * x[i])
        
        # Enhanced dynamic Gaussian peaks with memory effects
        gauss_peaks = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(7):
                center = self.gauss_centers[i, j]
                height = self.gauss_heights[i, j]
                width = self.gauss_widths[i, j]
                # Memory effect from previous and next dimension
                mem_factor = 1.0 + 0.15 * np.sin(0.6 * x[max(0, i-1)] + 0.4 * x[min(self.dim-1, i+1)])
                peak_sum += height * np.exp(-0.5 * ((x[i] - center) / (width * mem_factor)) ** 2)
            gauss_peaks += peak_sum
        
        # Cross-dimensional cubic coupling
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        cubic_coupling += self.cubic_coeffs[i, j, k] * x[i] * x[j] * x[k]
        
        # Asymmetric conditioning with hyperchaotic scaling
        cond_scaling = 0.0
        for i in range(self.dim):
            # Hyperchaotic conditioning factor based on position and dimension
            cond_factor = 1.0 + 0.7 * np.sin(0.3 * x[i] + 0.4 * i + 0.2 * np.cos(0.5 * x[i]))
            cond_scaling += cond_factor * (x[i]**3) / (1.0 + np.exp(-x[i]))
        
        # Multi-scale harmonic potential with temporal modulation
        harmonic_pot = 0.0
        for i in range(self.dim):
            # Temporal factor affects frequency and amplitude with higher variation
            temp_freq = 3.0 + 0.7 * np.sin(0.15 * self.time_factor + 0.2 * i)
            temp_amp = 2.0 + 0.4 * np.cos(0.25 * self.time_factor + 0.3 * i)
            harmonic_pot += temp_amp * np.sin(temp_freq * x[i]) * np.cos(0.5 * x[i])
        
        # Combine all components with dynamic weighting
        dim_factor = 1.0 + 0.3 * np.log(self.dim) + 0.15 * np.cos(0.4 * self.dim)
        return (0.20 * sine_mod + 0.35 * gauss_peaks + 0.15 * cubic_coupling + 
                0.20 * cond_scaling + 0.10 * harmonic_pot) * dim_factor