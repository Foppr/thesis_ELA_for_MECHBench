import numpy as np

class FractalSinusoidalAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.sinusoidal_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.amplitude_modulators = np.random.uniform(0.5, 2.0, dim)
        self.fractal_noise_levels = np.random.uniform(0.1, 0.5, dim)
        self.asymmetry_parameters = np.random.uniform(0.1, 0.9, dim)
        self.wavelet_scales = np.random.uniform(0.5, 2.0, dim)
        self.basin_depths = np.random.uniform(1.0, 3.0, dim)
        # Global parameters
        self.global_scale = np.random.uniform(0.5, 2.0)
        self.fractal_dimension = np.random.uniform(1.1, 1.8)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add sinusoidal components with fractal modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.sinusoidal_frequencies[i]
            amp_mod = self.amplitude_modulators[i]
            
            # Base sinusoidal term
            sin_term = np.sin(freq * xi) * np.cos(0.5 * freq * xi)
            
            # Fractal noise modulation
            fractal_noise = self.fractal_noise_levels[i] * np.sin(xi**2) * np.cos(xi)
            
            # Asymmetric gradient flow component
            asymmetry = self.asymmetry_parameters[i]
            asym_term = asymmetry * np.sin(freq * xi) * np.tanh(xi) * (1.0 + 0.1 * xi**2)
            
            result += amp_mod * (sin_term + fractal_noise + asym_term)
        
        # Add basin of attraction terms with varying depths
        for i in range(self.dim):
            xi = x[i]
            depth = self.basin_depths[i]
            # Multi-modal basin structure with fractal scaling
            basin_term = depth * np.exp(-0.5 * (xi / (1.0 + 0.2 * np.abs(xi)))**2) * np.sin(2.0 * xi)
            result += basin_term
        
        # Add cross-dimensional wavelet-like interactions
        for i in range(self.dim):
            xi = x[i]
            scale_i = self.wavelet_scales[i]
            wavelet_i = np.exp(-0.5 * (xi / scale_i)**2) * np.sin(scale_i * xi)
            
            for j in range(i+1, self.dim):
                xj = x[j]
                scale_j = self.wavelet_scales[j]
                wavelet_j = np.exp(-0.5 * (xj / scale_j)**2) * np.sin(scale_j * xj)
                
                # Interaction term with fractal coupling
                interaction = 0.5 * (1.0 + np.cos(0.3 * (i - j))) * wavelet_i * wavelet_j
                result += interaction
        
        # Add global fractal scaling and modulation
        fractal_scaling = np.power(np.sum(np.abs(x)), self.fractal_dimension)
        result *= self.global_scale * (1.0 + 0.1 * fractal_scaling)
        
        # Add asymmetric multi-modal structure with enhanced complexity
        multimodal_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multimodal term with polynomial and trigonometric interactions
            poly_term = xi**4 - 12*xi**2 + 36
            trig_term = np.sin(0.7 * xi) * np.cos(0.3 * xi)
            multimodal_component += poly_term * trig_term
        
        result += 0.5 * multimodal_component
        
        # Add fractal noise with chaotic perturbation
        chaotic_noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic noise with fractal characteristics
            chaotic_noise += np.sin(100.0 * xi) * np.cos(50.0 * xi) * np.exp(-0.05 * xi**2)
        
        result += 0.05 * chaotic_noise
        
        return result