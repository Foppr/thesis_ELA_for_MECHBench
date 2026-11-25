import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic force field with multiple frequencies
        force_field = 0.0
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * np.sin(2.0 * x_scaled[i])
            freq2 = 1.5 + 1.0 * np.cos(3.0 * x_scaled[i])
            force_field += np.sin(freq1 * x_scaled[i]) * np.cos(freq2 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Multi-scale gradient coupling with exponential decay
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                coupling = np.sin(8.0 * dist) * np.cos(6.0 * dist) * np.exp(-dist**2)
                gradient_mod += coupling * (1.0 + 0.4 * np.sin(15.0 * dist))
        
        # Complex multi-modal component with dynamic amplitude and phase
        modal_component = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.8 * np.sin(5.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i])
            phase = 2.0 * np.sin(x_scaled[i]**2)
            modal_component += amp * np.sin(4.0 * x_scaled[i] + phase) * np.cos(3.0 * x_scaled[i] - phase)
        
        # Radial exponential decay with chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_decay = np.exp(-r**2 / 3.0) * (1.0 + 0.3 * np.sin(10.0 * r))
        
        # Cross-dimensional coupling with dynamic weights
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = np.sin(4.0 * (x_scaled[i] + x_scaled[j])) * np.cos(3.0 * (x_scaled[i] - x_scaled[j]))
                    cross_dim += coupling / (1.0 + np.abs(x_scaled[i] - x_scaled[j])**2)
        
        # Combine all terms with dynamic weights
        result = radial_decay * (quadratic + 0.4 * force_field + 0.5 * gradient_mod + 0.6 * modal_component + 0.3 * cross_dim)
        
        # Add chaotic noise for increased complexity
        result += 0.02 * np.random.uniform(-1.0, 1.0)
        
        return result