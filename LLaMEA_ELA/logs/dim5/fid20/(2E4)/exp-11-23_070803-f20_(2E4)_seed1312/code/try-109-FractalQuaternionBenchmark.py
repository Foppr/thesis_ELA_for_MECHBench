import numpy as np

class FractalQuaternionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Fractal-like self-similarity component with recursive scaling
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Recursive fractal pattern with diminishing scale
            scale = 1.0
            for depth in range(1, 4):
                scale *= 0.5
                fractal_component += scale * np.sin(2**depth * xi) * np.cos(3**depth * xi)
        
        # Hyperbolic tangent gradient field with directional bias
        tanh_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Directional bias based on dimension index
            bias = np.tanh(i * 0.5) + 0.5
            tanh_component += np.tanh(3 * xi) * bias * (1 + 0.3 * np.sin(2*i))
        
        # Quaternion-based rotational symmetry component
        quat_component = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi, yi = x_norm[i], x_norm[i+1]
                # 2D rotational symmetry with quaternion-like structure
                angle = np.arctan2(yi, xi)
                radius = np.sqrt(xi**2 + yi**2)
                quat_component += (radius * np.cos(3 * angle) + 
                                 radius * np.sin(4 * angle)) * (1 + 0.2 * np.cos(i))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponential decay interaction with angular dependence
                distance = abs(x_norm[i] - x_norm[j])
                angle_diff = np.abs(np.arctan2(x_norm[j], x_norm[i]) - 
                                  np.arctan2(x_norm[i], x_norm[j]))
                strength = np.exp(-distance * 0.5) * (1 + 0.3 * np.cos(angle_diff))
                cross_coupling += strength * np.sin(5 * (x_norm[i] + x_norm[j]))
        
        # Multi-scale periodic modulation with frequency warping
        periodic_component = 0
        frequencies = [1, 2, 3, 5, 7]
        for i, freq in enumerate(frequencies):
            if i < self.dim:
                xi = x_norm[i]
                # Warped frequency based on dimension index
                warped_freq = freq * (1 + 0.2 * np.sin(i * np.pi / self.dim))
                periodic_component += np.sin(warped_freq * xi) * np.cos(2 * warped_freq * xi)
        
        # Asymmetric saddle-point landscape with cubic terms
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Cubic term with asymmetric bias
            cubic_term = xi**3 + 0.3 * xi**2 - 0.5 * xi
            # Asymmetric modulation based on dimension
            asym_mod = 1 + 0.4 * np.sin(2*i) * np.cos(i)
            saddle_component += cubic_term * asym_mod
        
        # Combine all components with adaptive weights
        result = 1.2 * fractal_component + 1.5 * tanh_component + 1.8 * quat_component + \
                1.0 * cross_coupling + 1.3 * periodic_component + 1.1 * saddle_component
        
        # Add controlled noise for robustness
        noise = np.random.normal(0, 0.002)
        
        return result + noise