import numpy as np

class FractalRBFMixtureLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Perturbed fractal scaling factors with harmonic frequency modulation
        self.fractal_factors = [np.sqrt(i + 1) * np.sin(i * 0.7) for i in range(dim)]
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced Radial Basis Function components with dynamic widths and heights
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(15, self.dim))
        for i in range(min(15, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.3 / (i + 1) ** 0.7
            height = 1.5 / (i + 1)**1.2
            distance = np.sum((x_norm - center)**2)
            rbf_sum += height * np.exp(-distance / (2 * width**2))
        
        # Modified fractal-like curvature with perturbed scaling and harmonic modulation
        fractal_curvature = 0.0
        for i in range(self.dim):
            scaled_x = x_norm[i] * self.fractal_factors[i % len(self.fractal_factors)]
            fractal_curvature += np.sin(scaled_x**4) * np.cos(scaled_x**3) * (1 + 0.5 * np.sin(i * 1.3))
        
        # Enhanced asymmetric saddle points with perturbed coupling coefficients
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                diff = x_norm[i] - x_norm[j]
                # Perturbed exponential decay and modified coupling strength
                saddle += (diff**3) * np.exp(-abs(diff) * 0.8) * (i + j) / (self.dim + 1.5)
        
        # Improved peak attraction regions with directional bias and harmonic shifts
        peak_attraction = 0.0
        for i in range(self.dim):
            # Create asymmetric peaks with harmonic phase shifts
            peak_pos = np.sin(i * np.pi / self.dim + 0.3) * 0.4 + 0.1 * np.cos(i * 0.7)
            dist_from_peak = abs(x_norm[i] - peak_pos)
            peak_attraction += np.exp(-dist_from_peak**2 * 3.5) * (1 + 0.5 * np.sin(i * 1.2) * np.cos(i * 0.8))
        
        # Enhanced cross-dimensional interaction with perturbed polynomial coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Perturbed multi-scale polynomial coupling with modified exponents
                cross_interaction += (x_norm[i]**4 + x_norm[j]**4) * \
                                   np.sin(x_norm[i] * x_norm[j] * 1.2) * \
                                   (i + j) / (self.dim**1.3)
        
        # Combine all terms with adjusted weights for better balance
        result = 0.3 * rbf_sum + 0.18 * fractal_curvature + 0.27 * saddle + \
                 0.17 * peak_attraction + 0.08 * cross_interaction
        
        # Enhanced conditioning through mixed polynomial terms with perturbed exponents
        conditioning = 0.06 * np.sum(np.abs(x_norm)**5.5) + 0.02 * np.sum(x_norm**3.2)
        
        # Add a new multi-modal component to increase complexity
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(2.2 * np.pi * x_norm[i]) * np.cos(3.1 * np.pi * x_norm[i])
            
        return result + conditioning + 0.05 * multimodal