import numpy as np

class ChaoticRBFHypersineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = 2.0 + 3.0 * np.random.rand(dim)
        self.gaussian_centers = np.random.uniform(-4, 4, (dim, 5))
        self.gaussian_heights = 1.0 + 2.0 * np.random.rand(dim, 5)
        self.polynomial_coeffs = np.random.uniform(-1, 1, (dim, 3))
        # Time-varying chaotic factor
        self.time_factor = 1.0 + 0.5 * np.sin(0.1 * dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation with dynamic frequencies
        chaotic_sine = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.7 * i)
            amp = 1.0 + 0.5 * np.sin(0.4 * x[i])
            chaotic_sine += amp * np.sin(freq * x[i]) * np.cos(0.6 * x[i])
        
        # Dynamic Gaussian peaks with memory effects
        gaussian_peaks = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(5):
                center = self.gaussian_centers[i, j]
                height = self.gaussian_heights[i, j]
                # Add memory effect from previous dimension
                sigma = 0.5 + 0.3 * np.sin(0.2 * x[max(0, i-1)])
                peak_sum += height * np.exp(-0.5 * ((x[i] - center) / sigma) ** 2)
            gaussian_peaks += peak_sum
        
        # Cross-dimensional polynomial coupling with chaotic coefficients
        poly_coupling = 0.0
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(3):
                coeff = self.polynomial_coeffs[i, j] * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.4 * i)
                poly_term += coeff * (x[i] ** (j + 1))
            # Add cross-dimension interaction
            if i < self.dim - 1:
                cross_term = 0.5 * x[i] * x[i+1]
                poly_coupling += poly_term + cross_term
        
        # Asymmetric conditioning with time-varying scaling
        conditioning = 0.0
        for i in range(self.dim):
            # Time-dependent conditioning factor
            cond_factor = 1.0 + 0.3 * np.sin(0.2 * x[i]) + 0.2 * np.cos(0.5 * self.time_factor)
            # Asymmetric weighting based on position
            if x[i] >= 0:
                weight = 1.0 + 0.4 * np.sin(0.6 * x[i])
            else:
                weight = 1.0 + 0.3 * np.cos(0.5 * x[i])
            conditioning += cond_factor * weight * (x[i] ** 2) / (1.0 + np.exp(-x[i]))
        
        # Combine all components with dimension scaling
        dim_scaling = 1.0 + 0.2 * np.log(self.dim) + 0.1 * np.sin(0.3 * self.dim)
        return (0.35 * chaotic_sine + 0.30 * gaussian_peaks + 
                0.20 * poly_coupling + 0.15 * conditioning) * dim_scaling