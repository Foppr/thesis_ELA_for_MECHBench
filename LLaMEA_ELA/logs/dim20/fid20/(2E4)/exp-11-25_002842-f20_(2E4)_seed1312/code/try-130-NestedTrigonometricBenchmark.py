import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive parameters for each dimension
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        self.interference_strengths = np.random.uniform(0.1, 1.0, dim)
        self.harmonic_orders = np.random.randint(2, 6, dim)
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x / 5.0) * np.pi
        
        # Base trigonometric components with varying frequencies and amplitudes
        base_terms = np.zeros(self.dim)
        for i in range(self.dim):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            phase = self.phase_offsets[i]
            order = self.harmonic_orders[i]
            
            # Nested harmonic structure with increasing complexity
            term = amp * np.sin(freq * x_norm[i] + phase)
            for _ in range(order - 1):
                term = amp * np.sin(freq * term + phase)
                
            base_terms[i] = term
            
        # Spatial interference patterns between dimensions
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling based on spatial distance and interference strength
                dist = np.abs(x[i] - x[j])
                coupling = self.interference_strengths[i] * np.exp(-dist**2 / (2 * (i + 1)**2))
                interference += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Multi-scale modulation with adaptive frequency components
        modulation = 0.0
        for i in range(self.dim):
            # Adaptive scaling based on dimension index and input value
            scale_factor = (i + 1) * (1 + 0.1 * np.sin(x[i]))
            mod_freq = self.frequencies[i] * (1 + 0.2 * np.cos(x[i]))
            modulation += np.sin(mod_freq * x_norm[i]) * np.cos(scale_factor * x_norm[i])
            
        # Boundary-sensitive transformation with asymmetric harmonic behavior
        boundary_effects = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_effects += np.sin(x[i]**2) * np.exp(-x[i]) * (1 + 0.3 * np.cos(x[i]))
            else:
                boundary_effects += np.cos(x[i]**2) * np.exp(-x[i]/2) * (1 + 0.3 * np.sin(x[i]))
                
        # Final composite function with weighted components
        return (0.4 * np.sum(base_terms**2) + 
                0.3 * interference + 
                0.2 * modulation + 
                0.1 * boundary_effects)