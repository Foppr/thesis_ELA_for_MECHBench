import numpy as np

class FractalSinusoidalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.sinusoidal_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.amplitude_modulators = np.random.uniform(0.3, 2.5, dim)
        self.fractal_noise_levels = np.random.uniform(0.05, 0.6, dim)
        self.asymmetry_parameters = np.random.uniform(0.05, 1.0, dim)
        self.wavelet_scales = np.random.uniform(0.3, 2.5, dim)
        self.basin_depths = np.random.uniform(0.8, 3.5, dim)
        # Global parameters
        self.global_scale = np.random.uniform(0.4, 2.2)
        self.fractal_dimension = np.random.uniform(1.0, 2.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add sinusoidal components with enhanced fractal modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.sinusoidal_frequencies[i]
            amp_mod = self.amplitude_modulators[i]
            
            # Enhanced sinusoidal term with additional harmonics
            sin_term = np.sin(freq * xi) * np.cos(0.5 * freq * xi) + 0.3 * np.sin(2.0 * freq * xi)
            
            # Improved fractal noise modulation
            fractal_noise = self.fractal_noise_levels[i] * np.sin(xi**1.5) * np.cos(xi**0.5)
            
            # Enhanced asymmetric gradient flow component
            asymmetry = self.asymmetry_parameters[i]
            asym_term = asymmetry * np.sin(freq * xi) * np.tanh(xi) * (1.0 + 0.15 * xi**2)
            
            result += amp_mod * (sin_term + fractal_noise + asym_term)
        
        # Enhanced basin of attraction terms with varying depths
        for i in range(self.dim):
            xi = x[i]
            depth = self.basin_depths[i]
            # Improved multi-modal basin structure with more complex scaling
            basin_term = depth * np.exp(-0.5 * (xi / (1.0 + 0.3 * np.abs(xi)))**2) * np.sin(2.0 * xi) * np.cos(0.5 * xi)
            result += basin_term
        
        # Enhanced cross-dimensional wavelet-like interactions
        for i in range(self.dim):
            xi = x[i]
            scale_i = self.wavelet_scales[i]
            wavelet_i = np.exp(-0.5 * (xi / scale_i)**2) * np.sin(scale_i * xi)
            
            for j in range(i+1, self.dim):
                xj = x[j]
                scale_j = self.wavelet_scales[j]
                wavelet_j = np.exp(-0.5 * (xj / scale_j)**2) * np.sin(scale_j * xj)
                
                # Enhanced interaction term with stronger fractal coupling
                interaction = 0.7 * (1.0 + np.cos(0.4 * (i - j))) * wavelet_i * wavelet_j
                result += interaction
        
        # Enhanced global fractal scaling and modulation
        fractal_scaling = np.power(np.sum(np.abs(x)), self.fractal_dimension)
        result *= self.global_scale * (1.0 + 0.15 * fractal_scaling)
        
        # Enhanced multimodal structure with additional complexity
        multimodal_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multimodal term with higher-order polynomial and trigonometric interactions
            poly_term = xi**4 - 10*xi**2 + 25
            trig_term = np.sin(0.8 * xi) * np.cos(0.4 * xi) + 0.2 * np.sin(3.0 * xi)
            multimodal_component += poly_term * trig_term
        
        result += 0.6 * multimodal_component
        
        # Enhanced fractal noise with stronger chaotic perturbation
        chaotic_noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Stronger chaotic noise with more complex fractal characteristics
            chaotic_noise += np.sin(120.0 * xi) * np.cos(60.0 * xi) * np.exp(-0.03 * xi**2)
        
        result += 0.08 * chaotic_noise
        
        return result