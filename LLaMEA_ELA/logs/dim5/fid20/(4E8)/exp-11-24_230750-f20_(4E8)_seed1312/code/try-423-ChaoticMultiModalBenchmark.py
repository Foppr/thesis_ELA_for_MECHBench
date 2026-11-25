import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine-wave modulation parameters with fractal-like structure
        self.sin_freq = 2.0 + 5.0 * np.random.rand(dim)
        self.sin_amp = 1.0 + 3.0 * np.random.rand(dim)
        # Dynamic Gaussian peak parameters with fractal-like distribution
        self.gauss_centers = np.random.uniform(-4.5, 4.5, (dim, 9))
        self.gauss_heights = 2.0 + 5.0 * np.random.rand(dim, 9)
        self.gauss_widths = 0.2 + 1.5 * np.random.rand(dim, 9)
        # Cross-dimensional fractal coupling coefficients with memory effects
        self.fractal_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim, dim))
        # Time-varying conditioning factors with enhanced chaos and noise
        self.time_factor = 2.0 + 0.8 * np.sin(0.2 * dim)
        # Adaptive noise injection parameters
        self.noise_amp = 0.1 + 0.3 * np.random.rand()
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like chaotic sine-wave modulation component
        sine_mod = 0.0
        for i in range(self.dim):
            mod_freq = self.sin_freq[i] * (1.0 + 0.4 * np.sin(0.5 * x[i] + 0.3 * i + 0.2 * np.cos(0.6 * x[i])))
            mod_amp = self.sin_amp[i] * (1.0 + 0.3 * np.cos(0.6 * x[i] + 0.4 * i + 0.1 * np.sin(0.7 * x[i])))
            sine_mod += mod_amp * np.sin(mod_freq * x[i])
        
        # Fractal-like dynamic Gaussian peaks with memory effects and adaptive conditioning
        gauss_peaks = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(9):
                center = self.gauss_centers[i, j]
                height = self.gauss_heights[i, j]
                width = self.gauss_widths[i, j]
                # Memory effect from previous and next dimension with fractal scaling
                mem_factor = 1.0 + 0.2 * np.sin(0.7 * x[max(0, i-1)] + 0.5 * x[min(self.dim-1, i+1)] + 0.3 * np.cos(0.4 * x[i]))
                # Fractal scaling factor
                fractal_scale = 1.0 + 0.15 * np.sin(0.8 * x[i] + 0.6 * i)
                peak_sum += height * np.exp(-0.5 * ((x[i] - center) / (width * mem_factor * fractal_scale)) ** 2)
            gauss_peaks += peak_sum
        
        # Fractal-like cross-dimensional coupling with memory and chaotic scaling
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        # Fractal coefficient with chaotic scaling
                        coeff = self.fractal_coeffs[i, j, k] * (1.0 + 0.25 * np.sin(0.6 * x[i] + 0.4 * x[j] + 0.3 * x[k]))
                        fractal_coupling += coeff * x[i] * x[j] * x[k]
        
        # Asymmetric conditioning with hyperchaotic scaling and fractal memory
        cond_scaling = 0.0
        for i in range(self.dim):
            # Hyperchaotic conditioning factor based on position, dimension, and memory
            cond_factor = 1.0 + 0.8 * np.sin(0.4 * x[i] + 0.5 * i + 0.3 * np.cos(0.6 * x[i]) + 0.2 * np.sin(0.7 * x[max(0, i-1)]))
            cond_scaling += cond_factor * (x[i]**3) / (1.0 + np.exp(-x[i]))
        
        # Multi-scale harmonic potential with fractal temporal modulation and noise
        harmonic_pot = 0.0
        for i in range(self.dim):
            # Fractal temporal factor affecting frequency and amplitude
            temp_freq = 2.5 + 0.8 * np.sin(0.2 * self.time_factor + 0.3 * i + 0.1 * np.cos(0.5 * x[i]))
            temp_amp = 1.5 + 0.5 * np.cos(0.3 * self.time_factor + 0.4 * i + 0.2 * np.sin(0.6 * x[i]))
            # Add adaptive noise
            noise = self.noise_amp * np.random.normal(0, 1)
            harmonic_pot += temp_amp * np.sin(temp_freq * x[i]) * np.cos(0.5 * x[i]) + noise
        
        # Combine all components with fractal weighting and dynamic scaling
        dim_factor = 1.0 + 0.4 * np.log(self.dim) + 0.2 * np.cos(0.5 * self.dim)
        # Add a novel fractal-like component for increased complexity
        fractal_component = 0.05 * np.sum([np.sin(3.0 * x[i] + 0.5 * i) * np.cos(2.0 * x[i]) for i in range(self.dim)])
        
        return (0.25 * sine_mod + 0.30 * gauss_peaks + 0.18 * fractal_coupling + 
                0.22 * cond_scaling + 0.05 * harmonic_pot + fractal_component) * dim_factor