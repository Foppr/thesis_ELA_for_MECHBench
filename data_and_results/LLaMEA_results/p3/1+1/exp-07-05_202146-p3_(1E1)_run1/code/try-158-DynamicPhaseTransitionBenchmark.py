import numpy as np

class DynamicPhaseTransitionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize dynamic phase parameters
        self.phase_params = np.random.uniform(0.5, 2.0, dim)
        self.correlation_decay = np.exp(-np.arange(dim) * 0.1)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.5 * np.sum(x**2)
        
        # Asymmetric saddle point structure with dynamic weights
        saddle_term = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(i * 0.7)
            saddle_term += weight * x[i]**2 * np.cos(x[i] * self.phase_params[i])
        result += 0.3 * saddle_term
        
        # Exponentially decaying correlation structure
        corr_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = self.correlation_decay[i] * self.correlation_decay[j]
                corr_sum += corr * x[i] * x[j] * np.sin(x[i] + x[j])
        result += 0.2 * corr_sum
        
        # Dynamic phase transition component
        phase_transition = 0.0
        for i in range(self.dim):
            phase = np.sin(x[i] * self.phase_params[i] + np.sum(x) * 0.1)
            phase_transition += phase * np.exp(-0.1 * np.abs(x[i]))
        result += 0.4 * phase_transition
        
        # Multi-scale oscillatory terms with varying amplitudes
        oscillation_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            oscillation_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        result += 0.25 * oscillation_sum
        
        # Memory-dependent basin structure
        if hasattr(self, 'prev_x'):
            memory_effect = 0.0
            for i in range(self.dim):
                memory_effect += 0.1 * (x[i] - self.prev_x[i])**2 * np.sin(x[i])
            result += memory_effect
        self.prev_x = x.copy()
        
        # Add global minimum attractor with dynamic strength
        min_attractor = 0.0
        for i in range(self.dim):
            min_attractor += 0.05 * (x[i] - 1.0)**2 * np.exp(-0.5 * (x[i] - 1.0)**2)
        result += min_attractor
        
        # Introduce chaotic basin boundaries with time-varying parameters
        chaotic_boundary = 0.0
        for i in range(self.dim):
            boundary = np.sin(x[i] * (1.0 + 0.1 * np.sin(np.sum(x))))
            chaotic_boundary += boundary * np.exp(-0.05 * np.abs(x[i]))
        result += 0.15 * chaotic_boundary
        
        # Add high-order interaction terms
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    interaction_sum += 0.02 * x[i] * x[j] * x[k] * np.cos(x[i] + x[j] + x[k])
        result += interaction_sum
        
        return result