import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic periodic force field with multiple frequencies
        force_field = 0.0
        for i in range(self.dim):
            # Higher frequency chaotic modulation with polynomial dependence
            freq = 4.0 + 3.0 * np.sin(6.0 * x_scaled[i]) + 0.7 * np.cos(8.0 * x_scaled[i]) + 0.2 * x_scaled[i]**3
            force_field += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Multi-scale cross-dimensional coupling with chaotic interactions and non-linear distance metrics
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Complex distance-based coupling with multiple chaotic factors and fractional powers
                dist = np.power(np.abs(x_scaled[i] - x_scaled[j]) + 0.01, 0.7)
                coupling = np.sin(9.0 * dist) * np.cos(7.0 * dist) * np.exp(-dist**3)
                gradient_mod += coupling * (1.0 + 0.5 * np.sin(17.0 * dist) * np.cos(14.0 * dist))
        
        # Enhanced multi-modal component with dynamic amplitude and phase
        modal_component = 0.0
        for i in range(self.dim):
            amp = 2.0 + 1.2 * np.sin(6.0 * x_scaled[i]) * np.cos(4.0 * x_scaled[i])
            phase = 2.5 * np.sin(5.0 * x_scaled[i]) + 0.7 * np.cos(7.0 * x_scaled[i])
            modal_component += amp * np.sin(5.0 * x_scaled[i] + phase) * np.cos(4.0 * x_scaled[i] + phase)
        
        # Advanced radial conditioning with exponential decay and logarithmic correction
        r = np.sqrt(np.sum(x_scaled**2))
        condition_factor = 1.0 + 4.0 * np.exp(-r**2 / 4.0) + 0.6 * np.sin(12.0 * r) * np.log(r + 1.0)
        
        # Additional high-order trigonometric coupling with complex phase relationships
        high_order_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_scaled[i] - x_scaled[j]
                high_order_coupling += np.sin(3.0 * diff) * np.cos(4.0 * diff) * np.tan(2.0 * diff) * np.exp(-np.abs(diff))
        
        # Combine all terms with dynamic weights and additional chaotic modulation
        result = condition_factor * (quadratic + 0.5 * force_field + 0.6 * gradient_mod + 0.7 * modal_component + 0.3 * high_order_coupling)
        
        # Add small chaotic noise for increased complexity and non-deterministic behavior
        result += 0.015 * np.random.uniform(-1.0, 1.0) * np.sin(20.0 * r)
        
        return result