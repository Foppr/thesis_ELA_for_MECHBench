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
            
            # Base sinusoidal term with higher frequency components
            sin_term = np.sin(freq * xi) * np.cos(0.5 * freq * xi) + 0.3 * np.sin(2.0 * freq * xi)
            
            # Enhanced fractal noise modulation
            fractal_noise = self.fractal_noise_levels[i] * (np.sin(xi**2) * np.cos(xi) + 0.2 * np.sin(xi**3))
            
            # Enhanced asymmetric gradient flow component
            asymmetry = self.asymmetry_parameters[i]
            asym_term = asymmetry * np.sin(freq * xi) * np.tanh(xi) * (1.0 + 0.15 * xi**2 + 0.05 * xi**4)
            
            result += amp_mod * (sin_term + fractal_noise + asym_term)
        
        # Add basin of attraction terms with varying depths and enhanced complexity
        for i in range(self.dim):
            xi = x[i]
            depth = self.basin_depths[i]
            # Enhanced multi-modal basin structure with fractal scaling
            basin_term = depth * np.exp(-0.5 * (xi / (1.0 + 0.3 * np.abs(xi)))**2) * np.sin(2.0 * xi)
            result += basin_term
        
        # Add cross-dimensional wavelet-like interactions with enhanced coupling
        for i in range(self.dim):
            xi = x[i]
            scale_i = self.wavelet_scales[i]
            wavelet_i = np.exp(-0.5 * (xi / scale_i)**2) * np.sin(scale_i * xi)
            
            for j in range(i+1, self.dim):
                xj = x[j]
                scale_j = self.wavelet_scales[j]
                wavelet_j = np.exp(-0.5 * (xj / scale_j)**2) * np.sin(scale_j * xj)
                
                # Enhanced interaction term with fractal coupling and asymmetry
                interaction = 0.3 * (1.0 + np.cos(0.4 * (i - j))) * wavelet_i * wavelet_j * (1.0 + 0.1 * xi * xj)
                result += interaction
        
        # Add global fractal scaling and modulation with enhanced complexity
        fractal_scaling = np.power(np.sum(np.abs(x)), self.fractal_dimension)
        result *= self.global_scale * (1.0 + 0.15 * fractal_scaling + 0.05 * np.sin(fractal_scaling))
        
        # Add enhanced multimodal structure with polynomial and trigonometric interactions
        multimodal_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multimodal term with higher-order polynomials and trigonometric interactions
            poly_term = xi**5 - 15*xi**3 + 50*xi**2 - 60*xi + 36
            trig_term = np.sin(0.8 * xi) * np.cos(0.4 * xi) + 0.2 * np.sin(1.5 * xi)
            multimodal_component += poly_term * trig_term
        
        result += 0.6 * multimodal_component
        
        # Add enhanced fractal noise with chaotic perturbation
        chaotic_noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic noise with fractal characteristics and asymmetry
            chaotic_noise += (np.sin(120.0 * xi) * np.cos(60.0 * xi) + 0.3 * np.cos(80.0 * xi)) * np.exp(-0.07 * xi**2)
        
        result += 0.07 * chaotic_noise
        
        return result