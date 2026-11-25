import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales with enhanced diversity
        self.scales = np.logspace(0, 2.5, min(6, dim), base=10)
        self.amplitudes = np.logspace(1.5, -0.5, min(6, dim), base=10)
        # Add more diverse frequency modulation factors
        self.freq_modulators = np.linspace(8.0, 15.0, min(6, dim))
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with modified condition number
        base = 0.5 * np.sum(x_scaled**2)
        
        # Enhanced multi-scale fractal component with improved self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Enhanced hierarchical frequency modulation based on scale and position
            scale_idx = min(i % len(self.scales), len(self.scales) - 1)
            freq = self.freq_modulators[scale_idx] * self.scales[scale_idx] * (1.0 + 0.4 * np.sin(3.0 * x_scaled[i]))
            
            # Enhanced amplitude modulation with dynamic scaling
            amp = self.amplitudes[scale_idx] * (1.0 + 0.2 * np.cos(2.0 * x_scaled[i]) + 0.1 * np.sin(5.0 * x_scaled[i]))
            
            # Fractal oscillation with improved self-similarity and multi-scale interaction
            fractal_term = amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]**2) * np.exp(-0.1 * np.abs(x_scaled[i]))
            fractal += fractal_term
        
        # Improved hierarchical valley structure with more complex nested minima
        valleys = 0.0
        for i in range(self.dim):
            # Create more diverse and challenging nested valleys
            valley1 = np.exp(-((x_scaled[i] - 0.6)**2 + (x_scaled[i] + 0.4)**2) / 0.04)
            valley2 = np.exp(-((x_scaled[i] + 0.8)**2 + (x_scaled[i] - 0.1)**2) / 0.02)
            valley3 = np.exp(-((x_scaled[i] - 0.2)**2 + (x_scaled[i] + 0.7)**2) / 0.06)
            valley4 = np.exp(-((x_scaled[i] + 0.3)**2 + (x_scaled[i] - 0.5)**2) / 0.08)
            valleys += valley1 + valley2 + valley3 + valley4
        
        # Enhanced cross-dimensional coupling with fractal interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range for complexity
                # Enhanced fractal coupling with scale-dependent interaction and phase modulation
                scale_factor = (self.scales[min(i, len(self.scales)-1)] + 
                              self.scales[min(j, len(self.scales)-1)]) / 2.0
                phase_shift = np.sin(0.5 * (x_scaled[i] - x_scaled[j]))
                coupling_term = np.sin(scale_factor * (x_scaled[i] + x_scaled[j]) + phase_shift) * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
                coupling += coupling_term
        
        # Enhanced scale-invariant complexity component with improved fractal dimensionality
        complexity = 0.0
        for i in range(self.dim):
            # Add enhanced fractal dimensionality through multi-scale sine waves with varying weights
            for k, scale in enumerate(self.scales[:min(4, len(self.scales))]):
                weight = 1.0 / (k + 1) ** 1.5  # Decreasing weights for higher scales
                complexity += weight * np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i]**2)
        
        # Enhanced dynamic weighting based on position with improved conditioning
        position_factor = 1.0 + 0.3 * np.sin(np.sum(x_scaled**2)) + 0.2 * np.cos(2.0 * np.sum(x_scaled**2))
        result = (base * position_factor + 
                 1.0 * fractal + 
                 1.5 * valleys + 
                 0.7 * coupling + 
                 0.5 * complexity)
        
        # Enhanced noise with better fractal characteristics and controlled amplitude
        noise_amp = 0.015 * (1.0 + 0.08 * np.sin(40.0 * np.sum(x_scaled**2)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise