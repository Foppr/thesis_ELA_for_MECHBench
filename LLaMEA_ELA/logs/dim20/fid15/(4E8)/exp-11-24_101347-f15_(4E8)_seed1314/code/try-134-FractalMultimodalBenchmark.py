import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 3, min(7, dim), base=10)
        self.amplitudes = np.logspace(1.5, -1.5, min(7, dim), base=10)
        self.frequency_modulators = np.linspace(0.5, 2.5, min(7, dim))
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive weighting
        base = np.sum(x_scaled**2) * (1.0 + 0.3 * np.sin(5.0 * np.sum(x_scaled)))
        
        # Multi-scale fractal component with enhanced chaotic behavior
        fractal = 0.0
        for i in range(self.dim):
            # Hierarchical frequency modulation based on scale and dimension
            scale_idx = min(i % len(self.scales), len(self.scales) - 1)
            freq = 20.0 * self.scales[scale_idx] * (1.0 + 0.8 * np.sin(3.0 * x_scaled[i] + 0.5 * i))
            
            # Multi-scale amplitude modulation with dynamic scaling
            amp = self.amplitudes[scale_idx] * (1.0 + 0.6 * np.cos(4.0 * x_scaled[i] + 0.3 * i))
            
            # Fractal oscillation with enhanced self-similarity and chaotic behavior
            fractal_term = amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]**2) * np.tanh(x_scaled[i])
            fractal += fractal_term
        
        # Enhanced hierarchical valley structure with multiple nested minima and chaotic positioning
        valleys = 0.0
        for i in range(self.dim):
            # Create multiple nested valleys with modified Gaussian shapes and chaotic offsets
            offset1 = 0.5 * np.sin(2.0 * i) + 0.3 * np.cos(1.5 * i)
            offset2 = -0.4 * np.cos(2.5 * i) + 0.2 * np.sin(1.2 * i)
            offset3 = 0.6 * np.sin(1.8 * i) - 0.3 * np.cos(2.2 * i)
            
            valley1 = np.exp(-((x_scaled[i] - 0.6 + offset1)**2 + (x_scaled[i] + 0.4 + offset2)**2) / 0.03)
            valley2 = np.exp(-((x_scaled[i] + 0.8 + offset3)**2 + (x_scaled[i] - 0.1 - offset1)**2) / 0.025)
            valley3 = np.exp(-((x_scaled[i] - 0.2 + offset2)**2 + (x_scaled[i] + 0.8 - offset3)**2) / 0.04)
            valleys += valley1 + valley2 + valley3
        
        # Cross-dimensional coupling with enhanced fractal interactions and chaotic coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range
                # Fractal coupling with scale-dependent interaction and chaotic modulation
                scale_factor = (self.scales[min(i, len(self.scales)-1)] + 
                              self.scales[min(j, len(self.scales)-1)]) / 2.0
                
                # Chaotic coupling modulation based on dimension indices
                chaos_mod = 1.0 + 0.5 * np.sin(2.0 * i + 0.7 * j) * np.cos(1.5 * i - 0.3 * j)
                
                coupling_term = chaos_mod * np.sin(scale_factor * (x_scaled[i] + x_scaled[j])) * np.cos(2.0 * scale_factor * x_scaled[i])
                coupling += coupling_term * np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Scale-invariant complexity component with enhanced fractal dimensionality and chaotic scaling
        complexity = 0.0
        for i in range(self.dim):
            # Add fractal dimensionality through multi-scale sine waves with modified frequencies and chaotic scaling
            for scale in self.scales[:min(5, len(self.scales))]:
                # Chaotic frequency modulation based on dimension index
                freq_mod = 1.0 + 0.4 * np.sin(3.0 * i + 0.2 * scale)
                complexity += freq_mod * np.sin(1.8 * scale * x_scaled[i]) * np.cos(1.4 * scale * x_scaled[i]**2)
        
        # Enhanced gradient modulation with chaotic behavior
        gradient_mod = 1.0 + 0.7 * np.sin(4.0 * np.sum(x_scaled**3) + 0.5 * np.sum(x_scaled))
        
        # Combine all components with dynamic weighting based on position and chaotic factors
        position_factor = 1.0 + 0.8 * np.sin(np.sum(x_scaled**4))  # Changed to quartic term
        result = (base * gradient_mod * position_factor + 
                 1.2 * fractal + 
                 1.5 * valleys + 
                 0.9 * coupling + 
                 0.7 * complexity)
        
        # Add noise with enhanced fractal characteristics and chaotic amplitude modulation
        noise_amp = 0.03 * (1.0 + 0.2 * np.sin(80.0 * np.sum(x_scaled**2)) * np.cos(60.0 * np.sum(x_scaled)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise