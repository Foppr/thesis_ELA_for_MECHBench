import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 2, min(5, dim), base=10)
        self.amplitudes = np.logspace(1, -1, min(5, dim), base=10)
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term
        base = np.sum(x_scaled**2)
        
        # Multi-scale fractal component with self-similar oscillations
        fractal = 0.0
        for i in range(self.dim):
            # Hierarchical frequency modulation based on scale
            scale_idx = min(i % len(self.scales), len(self.scales) - 1)
            freq = 10.0 * self.scales[scale_idx] * (1.0 + 0.5 * np.sin(2.0 * x_scaled[i]))
            
            # Multi-scale amplitude modulation
            amp = self.amplitudes[scale_idx] * (1.0 + 0.3 * np.cos(3.0 * x_scaled[i]))
            
            # Fractal oscillation with self-similarity
            fractal_term = amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]**2)
            fractal += fractal_term
        
        # Hierarchical valley structure with nested minima
        valleys = 0.0
        for i in range(self.dim):
            # Create multiple nested valleys
            valley1 = np.exp(-((x_scaled[i] - 0.5)**2 + (x_scaled[i] + 0.3)**2) / 0.05)
            valley2 = np.exp(-((x_scaled[i] + 0.7)**2 + (x_scaled[i] - 0.2)**2) / 0.03)
            valley3 = np.exp(-((x_scaled[i] - 0.1)**2 + (x_scaled[i] + 0.9)**2) / 0.07)
            valleys += valley1 + valley2 + valley3
        
        # Cross-dimensional coupling with fractal interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for scalability
                # Fractal coupling with scale-dependent interaction
                scale_factor = (self.scales[min(i, len(self.scales)-1)] + 
                              self.scales[min(j, len(self.scales)-1)]) / 2.0
                coupling_term = np.sin(scale_factor * (x_scaled[i] + x_scaled[j]))
                coupling += coupling_term * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Scale-invariant complexity component
        complexity = 0.0
        for i in range(self.dim):
            # Add fractal dimensionality through multi-scale sine waves
            for scale in self.scales[:min(3, len(self.scales))]:
                complexity += np.sin(scale * x_scaled[i]) * np.cos(scale * x_scaled[i]**2)
        
        # Combine all components with dynamic weighting based on position
        position_factor = 1.0 + 0.5 * np.sin(np.sum(x_scaled**2))
        result = (base * position_factor + 
                 0.8 * fractal + 
                 1.2 * valleys + 
                 0.6 * coupling + 
                 0.4 * complexity)
        
        # Add noise with fractal characteristics
        noise_amp = 0.02 * (1.0 + 0.1 * np.sin(50.0 * np.sum(x_scaled**2)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise