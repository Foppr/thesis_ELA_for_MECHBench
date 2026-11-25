import numpy as np

class HyperChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize highly chaotic parameters for each dimension
        self.chaos_params = 3.0 + 4.0 * np.random.rand(dim)
        self.gaussian_centers = np.random.uniform(-4.5, 4.5, (dim, 7))
        self.gaussian_heights = 1.5 + 3.0 * np.random.rand(dim, 7)
        self.polynomial_coeffs = np.random.uniform(-2, 2, (dim, 4))
        # Highly time-varying chaotic factor with multiple frequencies
        self.time_factor = 1.5 + 0.8 * np.sin(0.15 * dim) * np.cos(0.2 * dim)
        # Additional hyperchaotic parameters
        self.hyperchaos_params = 0.5 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic sine-wave modulation with multiple frequencies and memory effects
        chaotic_sine = 0.0
        for i in range(self.dim):
            freq1 = 2.5 + 3.5 * np.sin(0.7 * x[i]) + 0.5 * np.cos(0.9 * i)  # Slightly altered frequencies
            freq2 = 1.8 + 2.2 * np.sin(0.6 * x[i]) + 0.3 * np.sin(0.8 * i)
            amp1 = 1.7 + 0.7 * np.sin(0.4 * x[i])  # Modified amplitudes
            amp2 = 0.9 + 0.5 * np.cos(0.4 * x[i])
            # Add memory effect from multiple previous dimensions
            mem_factor = 0.4 * np.sin(0.15 * x[max(0, i-1)]) + 0.3 * np.cos(0.25 * x[max(0, i-2)])
            chaotic_sine += (amp1 * np.sin(freq1 * x[i]) * np.cos(0.6 * x[i]) + 
                           amp2 * np.sin(freq2 * x[i]) * np.sin(0.4 * x[i])) * mem_factor
        
        # Enhanced dynamic Gaussian peaks with multi-scale memory effects
        gaussian_peaks = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(7):
                center = self.gaussian_centers[i, j]
                height = self.gaussian_heights[i, j]
                # Multi-scale memory effect from previous dimensions
                sigma1 = 0.5 + 0.3 * np.sin(0.4 * x[max(0, i-1)])
                sigma2 = 0.3 + 0.2 * np.cos(0.3 * x[max(0, i-2)])
                sigma3 = 0.4 + 0.1 * np.sin(0.5 * x[max(0, i-3)])
                sigma = sigma1 * sigma2 * sigma3
                peak_sum += height * np.exp(-0.5 * ((x[i] - center) / sigma) ** 2)
            gaussian_peaks += peak_sum
        
        # Cross-dimensional cubic coupling with hyperchaotic coefficients
        poly_coupling = 0.0
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(4):
                coeff = self.polynomial_coeffs[i, j] * np.sin(0.35 * x[i]) + 0.25 * np.cos(0.45 * i)
                # Add hyperchaotic modulation to coefficients
                coeff *= (1.0 + 0.15 * np.sin(self.hyperchaos_params[i] * x[i]))
                poly_term += coeff * (x[i] ** (j + 1))
            # Add cross-dimension interaction with chaotic coupling
            if i < self.dim - 1:
                cross_term = 0.6 * x[i] * x[i+1] * np.sin(0.25 * x[i])  # Slightly modified coupling
                poly_coupling += poly_term + cross_term
        
        # Asymmetric conditioning with hyperchaotic scaling and memory
        conditioning = 0.0
        for i in range(self.dim):
            # Hyperchaotic conditioning factor
            cond_factor = 1.3 + 0.3 * np.sin(0.25 * x[i]) + 0.2 * np.cos(0.5 * self.time_factor) + 0.15 * np.sin(0.7 * x[max(0, i-1)])
            # Asymmetric weighting with hyperchaotic modification
            if x[i] >= 0:
                weight = 1.3 + 0.4 * np.sin(0.6 * x[i]) + 0.25 * np.cos(0.3 * x[max(0, i-1)])
            else:
                weight = 1.0 + 0.3 * np.cos(0.5 * x[i]) + 0.15 * np.sin(0.4 * x[max(0, i-2)])
            # Hyperchaotic modification to the quadratic term
            quad_term = (x[i] ** 2) / (1.0 + np.exp(-x[i])) * (1.0 + 0.25 * np.sin(0.4 * x[i]))
            conditioning += cond_factor * weight * quad_term
        
        # Combine all components with enhanced dimension scaling
        dim_scaling = 1.3 + 0.2 * np.log(self.dim) + 0.15 * np.sin(0.35 * self.dim) + 0.1 * np.cos(0.25 * self.dim)
        return (0.4 * chaotic_sine + 0.3 * gaussian_peaks + 
                0.2 * poly_coupling + 0.1 * conditioning) * dim_scaling