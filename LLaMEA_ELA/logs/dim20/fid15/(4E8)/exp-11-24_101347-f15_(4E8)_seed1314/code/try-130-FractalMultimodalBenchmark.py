import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Significantly enhanced fractal parameters with exponential scaling
        self.scales = np.logspace(0, 3.0, min(8, dim), base=10)
        self.amplitudes = np.logspace(2.0, -1.0, min(8, dim), base=10)
        # Increased frequency modulation diversity
        self.freq_modulators = np.linspace(12.0, 25.0, min(8, dim))
        # Additional phase and amplitude modulation parameters
        self.phase_shifts = np.linspace(0.1, 1.5, min(8, dim))
        self.amplitude_modulators = np.logspace(0.5, 2.0, min(8, dim), base=2)
    
    def f(self, x):
        # Scale input to [-1, 1] range with enhanced normalization
        x_scaled = x / 5.0
        
        # Enhanced base quadratic term with exponential conditioning
        base = 0.5 * np.sum(x_scaled**2) * (1.0 + 0.1 * np.sin(10.0 * np.sum(x_scaled**2)))
        
        # Highly enhanced multi-scale fractal component with exponential complexity
        fractal = 0.0
        for i in range(self.dim):
            scale_idx = min(i % len(self.scales), len(self.scales) - 1)
            freq = self.freq_modulators[scale_idx] * self.scales[scale_idx] * (1.0 + 0.6 * np.sin(5.0 * x_scaled[i]))
            
            # Enhanced amplitude modulation with exponential scaling
            amp = self.amplitudes[scale_idx] * (1.0 + 0.3 * np.cos(3.0 * x_scaled[i]) + 
                                               0.2 * np.sin(7.0 * x_scaled[i]) + 
                                               0.1 * np.cos(11.0 * x_scaled[i]))
            
            # Fractal oscillation with exponential self-similarity and multi-scale interaction
            fractal_term = amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]**2) * np.exp(-0.15 * np.abs(x_scaled[i]))
            fractal += fractal_term
        
        # Enhanced hierarchical valley structure with exponentially increasing complexity
        valleys = 0.0
        for i in range(self.dim):
            # Create exponentially more diverse and challenging nested valleys
            valley1 = np.exp(-((x_scaled[i] - 0.6)**2 + (x_scaled[i] + 0.4)**2) / 0.03)
            valley2 = np.exp(-((x_scaled[i] + 0.8)**2 + (x_scaled[i] - 0.1)**2) / 0.015)
            valley3 = np.exp(-((x_scaled[i] - 0.2)**2 + (x_scaled[i] + 0.7)**2) / 0.05)
            valley4 = np.exp(-((x_scaled[i] + 0.3)**2 + (x_scaled[i] - 0.5)**2) / 0.07)
            valley5 = np.exp(-((x_scaled[i] - 0.9)**2 + (x_scaled[i] + 0.2)**2) / 0.02)
            valley6 = np.exp(-((x_scaled[i] + 0.1)**2 + (x_scaled[i] - 0.8)**2) / 0.09)
            valleys += valley1 + valley2 + valley3 + valley4 + valley5 + valley6
        
        # Enhanced cross-dimensional coupling with exponential interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Further increased coupling range
                scale_factor = (self.scales[min(i, len(self.scales)-1)] + 
                              self.scales[min(j, len(self.scales)-1)]) / 2.0
                phase_shift = np.sin(0.8 * (x_scaled[i] - x_scaled[j]) + self.phase_shifts[min(i, len(self.phase_shifts)-1)])
                coupling_term = np.sin(scale_factor * (x_scaled[i] + x_scaled[j]) + phase_shift) * np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2))
                coupling += coupling_term
        
        # Enhanced scale-invariant complexity component with exponential fractal dimensionality
        complexity = 0.0
        for i in range(self.dim):
            # Add exponentially enhanced fractal dimensionality through multi-scale sine waves with varying weights
            for k, scale in enumerate(self.scales[:min(6, len(self.scales))]):
                weight = 1.0 / (k + 1) ** 2.0  # Even more aggressive weight decay
                complexity += weight * np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i]**2)
        
        # Enhanced dynamic weighting based on position with exponential conditioning
        position_factor = 1.0 + 0.4 * np.sin(np.sum(x_scaled**2)) + 0.3 * np.cos(3.0 * np.sum(x_scaled**2))
        result = (base * position_factor + 
                 1.5 * fractal + 
                 2.0 * valleys + 
                 1.0 * coupling + 
                 0.8 * complexity)
        
        # Exponentially enhanced noise with better fractal characteristics and controlled amplitude
        noise_amp = 0.03 * (1.0 + 0.15 * np.sin(60.0 * np.sum(x_scaled**2)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise