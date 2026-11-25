import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic force field with multiple frequencies and phase modulation
        force_field = 0.0
        for i in range(self.dim):
            freq1 = 6.0 + 4.0 * np.sin(3.0 * x_scaled[i])
            freq2 = 3.0 + 2.0 * np.cos(5.0 * x_scaled[i])
            phase1 = 2.0 * np.sin(4.0 * x_scaled[i])
            phase2 = 2.5 * np.cos(3.0 * x_scaled[i])
            force_field += (np.sin(freq1 * x_scaled[i] + phase1) * 
                           np.cos(freq2 * x_scaled[i] + phase2) * 
                           np.exp(-0.4 * x_scaled[i]**2))
        
        # Multi-scale gradient coupling with enhanced exponential decay
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.001)
                coupling = (np.sin(15.0 * dist) * np.cos(12.0 * dist) * 
                           np.exp(-dist**4) * (1.0 + 0.7 * np.sin(25.0 * dist)))
                gradient_mod += coupling * (1.0 + 0.8 * np.sin(15.0 * dist))
        
        # Complex multi-modal component with dynamic amplitude, phase, and frequency
        modal_component = 0.0
        for i in range(self.dim):
            amp = 3.0 + 2.0 * np.sin(7.0 * x_scaled[i]) * np.cos(5.0 * x_scaled[i])
            phase = 4.0 * np.sin(x_scaled[i]**2) + 2.0 * np.cos(x_scaled[i])
            freq = 6.0 + 3.0 * np.sin(3.0 * x_scaled[i])
            modal_component += amp * np.sin(freq * x_scaled[i] + phase) * np.cos(5.0 * x_scaled[i] - phase)
        
        # Radial exponential decay with enhanced chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_decay = np.exp(-r**4 / 5.0) * (1.0 + 0.6 * np.sin(20.0 * r) * np.cos(10.0 * r))
        
        # Cross-dimensional coupling with dynamic weights and higher-order interactions
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = (np.sin(8.0 * (x_scaled[i] + x_scaled[j])) * 
                               np.cos(7.0 * (x_scaled[i] - x_scaled[j])) *
                               np.exp(-0.6 * (x_scaled[i]**2 + x_scaled[j]**2)))
                    cross_dim += coupling / (1.0 + 0.4 * np.abs(x_scaled[i] - x_scaled[j])**4)
        
        # Combine all terms with adjusted dynamic weights
        result = radial_decay * (quadratic + 0.7 * force_field + 0.8 * gradient_mod + 
                                0.9 * modal_component + 0.5 * cross_dim)
        
        # Add enhanced chaotic noise for increased complexity
        noise = 0.05 * np.random.uniform(-1.0, 1.0) * (1.0 + 0.6 * np.sin(30.0 * r))
        result += noise
        
        return result