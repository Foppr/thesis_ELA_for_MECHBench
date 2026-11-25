import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic behavior and enhanced multimodality
        self.chaotic_parameters = np.random.uniform(0.1, 0.9, dim)
        self.saddle_points = np.random.uniform(-3.0, 3.0, dim)
        self.ridge_strengths = np.random.uniform(0.5, 2.5, dim)
        self.coupling_strengths = np.random.uniform(0.3, 1.5, dim)
        self.modulation_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.adaptive_scaling = np.random.uniform(0.8, 1.2, dim)
        self.noise_amplitudes = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic potential with exponential and sinusoidal components
        for i in range(self.dim):
            xi = x[i]
            chaotic_param = self.chaotic_parameters[i]
            saddle_point = self.saddle_points[i]
            
            # Enhanced chaotic interference term
            chaotic_term = np.exp(-chaotic_param * np.abs(xi)) * np.sin(5.0 * xi) + \
                          np.sin(3.0 * xi**2) * np.cos(2.0 * xi) + \
                          np.sin(0.5 * xi) * np.cos(0.3 * xi)
            
            # Saddle-point dominance with adaptive scaling
            saddle_contribution = -np.exp(-0.5 * (xi - saddle_point)**2) * \
                                np.sin(0.1 * xi**3) * self.adaptive_scaling[i]
            
            result += chaotic_term + saddle_contribution
            
        # Ridge structures with variable strength and orientation
        ridge_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            ridge_strength = self.ridge_strengths[i]
            
            # Multi-dimensional ridge with cross-coupling
            ridge_component = ridge_strength * np.exp(-0.5 * xi**2) * \
                             (np.sin(2.0 * xi)**2 + np.cos(3.0 * xi)**2)
            
            ridge_term += ridge_component
            
        result += ridge_term
        
        # Cross-dimensional coupling with enhanced nonlinearity
        coupling_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling_strength = self.coupling_strengths[i]
                
                # Enhanced coupling with chaotic modulation
                cross_coupling = coupling_strength * np.sin(xi * xj) * \
                                np.exp(-0.1 * (xi**2 + xj**2)) * \
                                np.cos(0.3 * (xi - xj)**2)
                
                coupling_term += cross_coupling
                
        result += coupling_term
        
        # Adaptive modulation with dynamic frequency components
        modulation_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.modulation_frequencies[i]
            noise_amp = self.noise_amplitudes[i]
            
            # Multi-frequency modulation with chaotic noise
            modulated_component = np.sin(freq * xi) * \
                                 np.cos(0.5 * xi**2) * \
                                 (1.0 + noise_amp * np.sin(10.0 * xi))
            
            modulation_term += modulated_component
            
        result += modulation_term
        
        # Add global chaotic scaling and fractal-like behavior
        global_oscillation = np.sum(np.sin(self.modulation_frequencies * x)**2)
        fractal_scaling = 1.0 + 0.3 * np.sin(0.2 * global_oscillation) * \
                         np.cos(0.4 * self.dim)
        
        result *= fractal_scaling
        
        return result