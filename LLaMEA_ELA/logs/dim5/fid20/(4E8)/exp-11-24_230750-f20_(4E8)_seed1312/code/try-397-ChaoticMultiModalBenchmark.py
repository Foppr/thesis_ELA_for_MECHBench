import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine-wave modulation parameters
        self.sin_freq = 2.0 + 3.0 * np.random.rand(dim)
        self.sin_amp = 1.0 + 2.0 * np.random.rand(dim)
        # Dynamic Gaussian peak parameters
        self.gauss_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.gauss_heights = 2.0 + 3.0 * np.random.rand(dim, 5)
        self.gauss_widths = 0.5 + 1.5 * np.random.rand(dim, 5)
        # Cross-dimensional polynomial coupling coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Time-varying conditioning factors
        self.time_factor = 1.0 + 0.3 * np.sin(0.1 * dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation component
        sine_mod = 0.0
        for i in range(self.dim):
            mod_freq = self.sin_freq[i] * (1.0 + 0.2 * np.sin(0.3 * x[i]))
            mod_amp = self.sin_amp[i] * (1.0 + 0.1 * np.cos(0.4 * x[i]))
            sine_mod += mod_amp * np.sin(mod_freq * x[i])
        
        # Dynamic Gaussian peaks with memory effects
        gauss_peaks = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(5):
                center = self.gauss_centers[i, j]
                height = self.gauss_heights[i, j]
                width = self.gauss_widths[i, j]
                # Memory effect from previous dimension
                mem_factor = 1.0 + 0.1 * np.sin(0.5 * x[max(0, i-1)])
                peak_sum += height * np.exp(-0.5 * ((x[i] - center) / (width * mem_factor)) ** 2)
            gauss_peaks += peak_sum
        
        # Cross-dimensional polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling += self.poly_coeffs[i, j] * x[i] * x[j]
        
        # Asymmetric conditioning with chaotic scaling
        cond_scaling = 0.0
        for i in range(self.dim):
            # Chaotic conditioning factor based on position and dimension
            cond_factor = 1.0 + 0.5 * np.sin(0.2 * x[i] + 0.3 * i)
            cond_scaling += cond_factor * (x[i]**2) / (1.0 + np.exp(-x[i]))
        
        # Multi-scale harmonic potential with temporal modulation
        harmonic_pot = 0.0
        for i in range(self.dim):
            # Temporal factor affects frequency and amplitude
            temp_freq = 2.0 + 0.5 * np.sin(0.1 * self.time_factor)
            temp_amp = 1.5 + 0.3 * np.cos(0.2 * self.time_factor)
            harmonic_pot += temp_amp * np.sin(temp_freq * x[i]) * np.cos(0.4 * x[i])
        
        # Combine all components with dynamic weighting
        dim_factor = 1.0 + 0.2 * np.log(self.dim) + 0.1 * np.cos(0.3 * self.dim)
        return (0.25 * sine_mod + 0.30 * gauss_peaks + 0.20 * poly_coupling + 
                0.15 * cond_scaling + 0.10 * harmonic_pot) * dim_factor