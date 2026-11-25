import numpy as np

class EnhancedChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.attractor_centers = np.random.uniform(-4.0, 4.0, dim)
        self.attractor_strengths = np.random.uniform(2.0, 6.0, dim)
        self.ridge_parameters = np.random.uniform(1.0, 3.0, dim)
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)
        self.frequency_modulators = np.random.uniform(1.0, 3.0, dim)
        # Additional chaotic and fractal parameters
        self.fractal_dimensions = np.random.uniform(1.2, 1.8, dim)
        self.saddle_strengths = np.random.uniform(1.0, 4.0, dim)
        self.coupling_exponents = np.random.uniform(0.3, 1.7, dim)
        # New chaotic and complex interaction parameters
        self.chaotic_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.multimodal_depths = np.random.uniform(0.8, 2.0, dim)
        self.interaction_scalers = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic attractor contributions with fractal modulation
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            ridge_param = self.ridge_parameters[i]
            fractal_dim = self.fractal_dimensions[i]
            
            # Fractal-like attractor with chaotic modulation
            distance = np.abs(xi - center)
            fractal_term = strength * np.exp(-0.5 * (distance / (1.0 + 0.2 * xi**2))**fractal_dim)
            
            # Add ridge-like gradient flow component with fractal scaling
            ridge_component = ridge_param * np.sin(4.0 * xi) * np.cos(3.0 * xi) * np.tanh(xi)
            
            result += fractal_term + ridge_component
            
        # Add chaotic saddle point contributions
        for i in range(self.dim):
            xi = x[i]
            saddle_strength = self.saddle_strengths[i]
            # Chaotic saddle point with exponential decay and higher-order terms
            saddle_term = saddle_strength * np.exp(-0.3 * xi**2) * np.sin(15.0 * xi) * np.cos(7.0 * xi)
            result += saddle_term
            
        # Add cross-dimensional coupling with adaptive fractal coupling and enhanced complexity
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Fractal-based coupling strength with new interaction pattern
                coupling_strength = 0.7 * (1.0 + np.sin(0.5 * (i - j))) * (1.0 + 0.3 * np.sin(xi + xj)) * (1.0 + 0.1 * np.cos(xi * xj))
                
                # Fractal coupling with power law interaction and additional trigonometric modulation
                exponent = self.coupling_exponents[i] * self.coupling_exponents[j]
                cross_term = coupling_strength * np.power(np.abs(xi - xj), exponent) * np.cos(0.7 * (xi + xj)) * np.sin(0.4 * (xi - xj))
                result += cross_term
                
        # Add dimensionally adaptive noise with fractal characteristics and new pattern
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i] * (1.0 + 0.3 * np.sin(0.8 * i)) * (1.0 + 0.2 * np.cos(xi)) * (1.0 + 0.1 * np.sin(xi**2))
            noise_component = noise_level * np.sin(15.0 * xi + 0.7 * i) * np.cos(8.0 * xi) * np.tanh(0.5 * xi)
            result += noise_component
            
        # Add frequency-dependent modulation for enhanced complexity with fractal scaling
        freq_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod += self.frequency_modulators[i] * np.sin(5.0 * xi + 0.4 * i) * np.tanh(xi) * np.cos(0.3 * xi)
        result += 0.15 * freq_mod**2
        
        # Add global scaling with non-linear transformation and fractal influence
        global_scale = 1.0 + 0.4 * np.tanh(np.sum(x) / self.dim) * np.prod(np.cos(x / 5.0)) * (1.0 + 0.2 * np.sin(np.sum(x)))
        result *= global_scale
        
        # Add chaotic perturbation to increase algorithmic bias - enhanced version
        chaotic_perturbation = 0.08 * np.sum(np.sin(120.0 * x) * np.cos(60.0 * x) * np.exp(-0.15 * np.sum(x**2)) * np.tanh(x))
        result += chaotic_perturbation
        
        # Add enhanced multi-modal structure with better fitness discrimination
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add multiple local minima with varying depths - mutated coefficients and pattern
            multimodal_term += (xi**5 - 20*xi**3 + 10*xi**2) * np.cos(0.6 * xi) * np.sin(0.4 * xi)
        result += 0.4 * multimodal_term
        
        # Mutated component: Increased complexity in the multimodal structure with new interaction terms
        enhanced_multimodal = 0.0
        for i in range(self.dim):
            xi = x[i]
            # New multimodal term with different polynomial and trigonometric components
            enhanced_multimodal += (xi**7 - 30*xi**5 + 20*xi**4) * np.sin(1.0 * xi) * np.cos(0.4 * xi) * np.tanh(xi)
        result += 0.3 * enhanced_multimodal
        
        # Additional mutation: Introduce more complex interaction between dimensions with new pattern
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                interaction_term += (xi**3 + xj**3) * np.sin(0.7 * (xi + xj)) * np.cos(0.3 * (xi - xj)) * np.exp(-0.1 * (xi**2 + xj**2))
        result += 0.15 * interaction_term
        
        # Add new complex chaotic component with multi-scale fractal influence
        fractal_chaos = 0.0
        for i in range(self.dim):
            xi = x[i]
            fractal_chaos += self.chaotic_amplitudes[i] * np.sin(20.0 * xi) * np.cos(10.0 * xi) * np.tanh(xi) * np.exp(-0.2 * xi**2)
        result += 0.25 * fractal_chaos
        
        # Add new multi-scale multimodal structure
        multi_scale_multimodal = 0.0
        for i in range(self.dim):
            xi = x[i]
            multi_scale_multimodal += (xi**8 - 35*xi**6 + 25*xi**5) * np.sin(0.9 * xi) * np.cos(0.5 * xi)
        result += 0.15 * multi_scale_multimodal
        
        # Add new component: Enhanced fractal modulation with improved fitness balance
        enhanced_fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            enhanced_fractal += np.sin(25.0 * xi) * np.cos(12.0 * xi) * np.tanh(xi) * (1.0 + 0.3 * np.sin(xi**2))
        result += 0.2 * enhanced_fractal
        
        # Add new component: Improved cross-dimensional interaction with better scaling
        improved_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                improved_cross += np.sin(0.5 * (xi + xj)) * np.cos(0.3 * (xi - xj)) * np.exp(-0.05 * (xi**2 + xj**2)) * (1.0 + 0.2 * np.sin(xi * xj))
        result += 0.1 * improved_cross
        
        # Add final complex component with better balancing of terms
        final_complex = 0.0
        for i in range(self.dim):
            xi = x[i]
            final_complex += (xi**6 - 25*xi**4 + 15*xi**3) * np.sin(0.8 * xi) * np.cos(0.6 * xi) * np.exp(-0.1 * xi**2)
        result += 0.1 * final_complex
        
        return result