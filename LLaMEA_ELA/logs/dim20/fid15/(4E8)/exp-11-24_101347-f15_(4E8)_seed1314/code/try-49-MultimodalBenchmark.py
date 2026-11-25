import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Modified periodic force field with altered frequencies
        force_field = 0.0
        for i in range(self.dim):
            # Modified frequency based on position
            freq = 2.5 + 2.0 * np.sin(4.0 * x_scaled[i])
            force_field += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Altered gradient modulation with different coupling
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified distance-based coupling
                dist = np.abs(x_scaled[i] - x_scaled[j])
                coupling = np.sin(6.0 * dist) * np.cos(8.0 * dist)
                gradient_mod += coupling * (1.0 + 0.4 * np.sin(15.0 * dist))
        
        # Modified multi-modal component with different amplitude modulation
        modal_component = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.6 * np.sin(5.0 * x_scaled[i])
            modal_component += amp * np.sin(4.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[i])
        
        # Adjusted adaptive conditioning based on distance from origin
        r = np.sqrt(np.sum(x_scaled**2))
        condition_factor = 1.0 + 3.0 * np.exp(-r**2 / 3.0)
        
        # Combine all terms with modified weights
        result = condition_factor * (quadratic + 0.4 * force_field + 0.5 * gradient_mod + 0.6 * modal_component)
        
        # Add small chaotic noise for increased complexity
        result += 0.01 * np.random.uniform(-1.0, 1.0)
        
        return result