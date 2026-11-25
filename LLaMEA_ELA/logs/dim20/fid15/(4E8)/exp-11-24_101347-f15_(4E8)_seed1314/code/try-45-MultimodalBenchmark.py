import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Periodic force field with modified chaotic modulation
        force_field = 0.0
        for i in range(self.dim):
            # Modified frequency based on position
            freq = 1.5 + 2.0 * np.sin(2.5 * x_scaled[i])
            force_field += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Chaotic gradient modulation with altered multi-scale interactions
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Altered distance-based coupling with different chaotic factor
                dist = np.abs(x_scaled[i] - x_scaled[j])
                coupling = np.sin(4.0 * dist) * np.cos(6.0 * dist)
                gradient_mod += coupling * (1.0 + 0.2 * np.sin(10.0 * dist))
        
        # Modified multi-modal component with altered amplitude
        modal_component = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.3 * np.sin(3.5 * x_scaled[i])
            modal_component += amp * np.sin(2.5 * x_scaled[i]) * np.cos(1.5 * x_scaled[i])
        
        # Modified adaptive conditioning based on distance from origin
        r = np.sqrt(np.sum(x_scaled**2))
        condition_factor = 1.0 + 1.5 * np.exp(-r**2 / 3.0)
        
        # Combine all terms with adjusted weights
        result = condition_factor * (quadratic + 0.4 * force_field + 0.3 * gradient_mod + 0.6 * modal_component)
        
        # Add small chaotic noise for increased complexity
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result