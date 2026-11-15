import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term with conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 6 + 1)  # Increased frequency range
            amp = 2.0 + 1.2 * np.sin(i * 0.7)  # Increased amplitude variation
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.4 * (x_normalized[i] - 0.15)**2)
        
        # Add a complex penalty term with multiple local minima and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.4 * (x_normalized[i]**12 - 6 * x_normalized[i]**10 + 15 * x_normalized[i]**8 - 20 * x_normalized[i]**6 + 15 * x_normalized[i]**4 - 6 * x_normalized[i]**2 + 1)
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.15 * np.sin(20 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
            
        # Add a highly oscillatory term to increase complexity with cross-dimension interactions
        oscillatory = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                oscillatory += 0.3 * np.sin(30 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(25 * np.pi * (x_normalized[i] - x_normalized[j]))
                
        # Add a central repulsion term to challenge basin attraction
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_normalized**2))
        center_repulsion = 3.0 * np.exp(-0.6 * dist_from_origin**2) * (1.0 + 0.7 * np.sin(15 * dist_from_origin))
        
        # Add a new chaotic component for increased complexity with modified parameters
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.35 * np.sin(55 * np.pi * x_normalized[i]) * np.cos(45 * np.pi * x_normalized[i]) * np.exp(-0.18 * x_normalized[i]**2)
        
        # Add a new term to improve fitness score and reduce bias
        bias_reduction = 0.0
        for i in range(self.dim):
            bias_reduction += 0.08 * np.sin(10 * np.pi * x_normalized[i]) * np.cos(8 * np.pi * x_normalized[i])
            
        # Add a new term to increase basin of attraction complexity
        basin_complexity = 0.0
        for i in range(self.dim):
            basin_complexity += 0.18 * np.sin(25 * np.pi * x_normalized[i]) * np.cos(20 * np.pi * x_normalized[i]) * np.exp(-0.25 * x_normalized[i]**2)
        
        # Add new cross-dimensional exponential interaction term with enhanced decay
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += 0.3 * np.exp(-3.0 * (x_normalized[i]**2 + x_normalized[j]**2)) * np.sin(40 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        # Add a new interaction term with adaptive frequency modulation
        adaptive_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                adaptive_interaction += 0.2 * np.sin(35 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(30 * np.pi * (x_normalized[i] - x_normalized[j])) * np.exp(-0.5 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Add a new penalty term with enhanced nonlinearity
        enhanced_penalty = 0.0
        for i in range(self.dim):
            enhanced_penalty += 0.5 * (x_normalized[i]**14 - 7 * x_normalized[i]**12 + 21 * x_normalized[i]**10 - 35 * x_normalized[i]**8 + 35 * x_normalized[i]**6 - 21 * x_normalized[i]**4 + 7 * x_normalized[i]**2 - 1)
        
        # Add new cubic cross-dimensional interaction term
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += 0.25 * (x_normalized[i]**3 + x_normalized[j]**3) * np.sin(20 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        # Add a new quartic cross-dimensional interaction term to increase landscape complexity
        quartic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quartic_interaction += 0.35 * (x_normalized[i]**4 + x_normalized[j]**4) * np.cos(25 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Add a new high-frequency chaotic component
        high_freq_chaos = 0.0
        for i in range(self.dim):
            high_freq_chaos += 0.4 * np.sin(80 * np.pi * x_normalized[i]) * np.cos(70 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Add a new multi-scale interaction term
        multi_scale = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multi_scale += 0.2 * np.sin(50 * np.pi * (x_normalized[i]**2 + x_normalized[j]**2)) * np.cos(40 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        # Add a new radial basis function component
        radial_basis = 0.0
        for i in range(self.dim):
            radial_basis += 0.3 * np.exp(-2.0 * (x_normalized[i]**2)) * np.sin(30 * np.pi * x_normalized[i])
        
        # Add a new cross-dimensional trigonometric interaction with variable phase
        trig_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = 0.5 * np.sin(i * 0.3) * np.cos(j * 0.4)
                trig_interaction += 0.28 * np.sin(35 * np.pi * (x_normalized[i] + x_normalized[j] + phase)) * np.cos(30 * np.pi * (x_normalized[i] - x_normalized[j] + phase))
        
        # Add a new polynomial interaction with variable coefficients
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += 0.15 * (x_normalized[i]**5 + x_normalized[j]**5) * np.sin(20 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Add a new term to increase the overall complexity and challenge
        complex_term = 0.0
        for i in range(self.dim):
            complex_term += 0.3 * np.sin(60 * np.pi * x_normalized[i]) * np.cos(50 * np.pi * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Add a new interaction term with higher-order polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += 0.25 * (x_normalized[i]**6 + x_normalized[j]**6) * np.sin(25 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Add a new chaotic interaction with dynamic frequency modulation
        dynamic_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_chaos += 0.3 * np.sin(40 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(35 * np.pi * (x_normalized[i] - x_normalized[j])) * np.exp(-0.4 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Add a new multi-modal penalty with variable scaling
        multi_modal_penalty = 0.0
        for i in range(self.dim):
            multi_modal_penalty += 0.4 * (x_normalized[i]**16 - 8 * x_normalized[i]**14 + 28 * x_normalized[i]**12 - 56 * x_normalized[i]**10 + 70 * x_normalized[i]**8 - 56 * x_normalized[i]**6 + 28 * x_normalized[i]**4 - 8 * x_normalized[i]**2 + 1)
        
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory + center_repulsion + chaotic + bias_reduction + basin_complexity + cross_exp + adaptive_interaction + enhanced_penalty + cubic_interaction + quartic_interaction + high_freq_chaos + multi_scale + radial_basis + trig_interaction + poly_interaction + complex_term + poly_coupling + dynamic_chaos + multi_modal_penalty